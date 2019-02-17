# Pioneer HDJ-500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.9; 49 -1.8; 54 -2.8; 60 -3.6; 66 -3.9; 72 -4.0; 79 -4.4; 87 -4.7; 96 -4.7; 106 -4.9; 116 -5.1; 128 -5.4; 141 -5.6; 155 -6.0; 170 -5.9; 187 -6.2; 206 -6.4; 227 -6.3; 249 -6.1; 274 -6.2; 302 -6.4; 332 -6.4; 365 -7.1; 402 -6.9; 442 -6.4; 486 -6.9; 535 -7.3; 588 -7.2; 647 -7.2; 712 -7.2; 783 -7.0; 861 -6.8; 947 -6.8; 1042 -6.3; 1146 -5.8; 1261 -5.1; 1387 -4.8; 1526 -4.2; 1678 -3.5; 1846 -2.1; 2031 -0.7; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -5.3; 5267 -8.6; 5793 -7.3; 6373 -6.9; 7010 -6.5; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.7; 16529 -8.1; 18182 -7.0; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Pioneer HDJ-500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pioneer HDJ-500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 29 Hz    | 0.57 | 6.4 dB  |
| Peaking | 903 Hz   | 0.78 | -2.2 dB |
| Peaking | 3473 Hz  | 0.53 | 8.3 dB  |
| Peaking | 5274 Hz  | 5.44 | -6.3 dB |
| Peaking | 6903 Hz  | 0.88 | -4.0 dB |
| Peaking | 2092 Hz  | 4.39 | 1.6 dB  |
| Peaking | 2885 Hz  | 0.86 | -0.7 dB |
| Peaking | 4418 Hz  | 8.56 | 2.4 dB  |
| Peaking | 16651 Hz | 2.53 | -1.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 1.8 dB  |
| Peaking | 125 Hz   | 1.41 | 0.5 dB  |
| Peaking | 250 Hz   | 1.41 | 0.1 dB  |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB |
| Peaking | 2000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Pioneer%20HDJ-500/Pioneer%20HDJ-500.png)