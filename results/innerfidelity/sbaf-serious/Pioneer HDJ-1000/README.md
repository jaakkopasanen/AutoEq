# Pioneer HDJ-1000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -1.3; 79 -2.7; 87 -3.9; 96 -4.8; 106 -5.1; 116 -5.1; 128 -5.2; 141 -5.2; 155 -5.1; 170 -4.9; 187 -4.9; 206 -4.9; 227 -4.7; 249 -4.4; 274 -4.0; 302 -3.8; 332 -3.7; 365 -3.4; 402 -2.9; 442 -2.7; 486 -3.7; 535 -4.2; 588 -3.8; 647 -4.4; 712 -5.1; 783 -5.5; 861 -6.1; 947 -6.3; 1042 -6.7; 1146 -7.2; 1261 -8.1; 1387 -9.0; 1526 -9.7; 1678 -9.6; 1846 -8.5; 2031 -6.9; 2234 -5.2; 2457 -3.3; 2703 -2.0; 2973 -0.6; 3270 -0.5; 3597 -0.7; 3957 -4.7; 4353 -4.6; 4788 -1.0; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Pioneer HDJ-1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pioneer HDJ-1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.58 | 6.8 dB  |
| Peaking | 420 Hz  | 1.03 | 3.4 dB  |
| Peaking | 1588 Hz | 2.06 | -4.4 dB |
| Peaking | 3026 Hz | 2.2  | 6.4 dB  |
| Peaking | 5676 Hz | 2.93 | 6.3 dB  |
| Peaking | 37 Hz   | 2.62 | -0.9 dB |
| Peaking | 66 Hz   | 2.77 | 2.0 dB  |
| Peaking | 101 Hz  | 2.26 | -1.3 dB |
| Peaking | 2395 Hz | 4.19 | 0.3 dB  |
| Peaking | 8289 Hz | 4.39 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 4.8 dB  |
| Peaking | 125 Hz   | 1.41 | -0.4 dB |
| Peaking | 250 Hz   | 1.41 | 1.7 dB  |
| Peaking | 500 Hz   | 1.41 | 3.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.5 dB |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Pioneer%20HDJ-1000/Pioneer%20HDJ-1000.png)