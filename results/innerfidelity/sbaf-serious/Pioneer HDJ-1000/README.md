# Pioneer HDJ-1000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -1.1; 66 -2.7; 72 -4.0; 79 -5.4; 87 -6.6; 96 -7.5; 106 -7.8; 116 -7.8; 128 -8.0; 141 -7.9; 155 -7.8; 170 -7.6; 187 -7.6; 206 -7.6; 227 -7.4; 249 -7.1; 274 -6.7; 302 -6.5; 332 -6.4; 365 -6.1; 402 -5.6; 442 -5.4; 486 -6.4; 535 -6.9; 588 -6.6; 647 -7.1; 712 -7.9; 783 -8.2; 861 -8.8; 947 -9.0; 1042 -9.4; 1146 -9.9; 1261 -10.8; 1387 -11.8; 1526 -12.4; 1678 -12.3; 1846 -11.2; 2031 -9.7; 2234 -7.9; 2457 -6.0; 2703 -4.7; 2973 -2.8; 3270 -2.1; 3597 -3.1; 3957 -7.4; 4353 -7.4; 4788 -3.6; 5267 -1.5; 5793 -2.2; 6373 -2.5; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Pioneer HDJ-1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pioneer HDJ-1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 59 Hz   | 0.33 | 10.6 dB  |
| Peaking | 108 Hz  | 0.65 | -10.3 dB |
| Peaking | 1533 Hz | 1.3  | -6.2 dB  |
| Peaking | 3072 Hz | 3.2  | 5.6 dB   |
| Peaking | 5743 Hz | 3.06 | 5.2 dB   |
| Peaking | 86 Hz   | 6.51 | -0.4 dB  |
| Peaking | 424 Hz  | 5.01 | 1.4 dB   |
| Peaking | 828 Hz  | 4.73 | -0.7 dB  |
| Peaking | 4153 Hz | 5.62 | -6.7 dB  |
| Peaking | 4178 Hz | 2.32 | 3.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.0 dB  |
| Peaking | 62 Hz    | 1.41 | 3.5 dB  |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -0.2 dB |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.6 dB |
| Peaking | 2000 Hz  | 1.41 | -3.5 dB |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Pioneer%20HDJ-1000/Pioneer%20HDJ-1000.png)