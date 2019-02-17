# Monster Jamz
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.6; 23 -12.6; 25 -12.5; 28 -12.3; 31 -12.2; 34 -12.1; 37 -11.9; 41 -11.8; 45 -11.6; 49 -11.5; 54 -11.3; 60 -11.2; 66 -11.1; 72 -11.0; 79 -10.9; 87 -10.9; 96 -10.8; 106 -10.6; 116 -10.3; 128 -10.1; 141 -9.9; 155 -9.6; 170 -9.3; 187 -8.9; 206 -8.5; 227 -8.1; 249 -7.6; 274 -7.2; 302 -6.7; 332 -6.3; 365 -5.8; 402 -5.4; 442 -4.9; 486 -4.6; 535 -4.3; 588 -3.6; 647 -3.5; 712 -3.4; 783 -3.2; 861 -3.5; 947 -3.9; 1042 -4.5; 1146 -5.2; 1261 -5.4; 1387 -5.8; 1526 -7.0; 1678 -7.9; 1846 -8.6; 2031 -9.2; 2234 -9.5; 2457 -8.9; 2703 -8.4; 2973 -5.2; 3270 -2.2; 3597 -0.7; 3957 -1.4; 4353 -4.2; 4788 -5.9; 5267 -5.4; 5793 -3.2; 6373 -0.5; 7010 -1.8; 7711 -4.0; 8482 -4.2; 9330 -4.3; 10263 -4.3; 11289 -4.3; 12418 -4.3; 13660 -4.3; 15026 -6.2; 16529 -4.3; 18182 -4.3; 20000 -4.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Jamz GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Jamz ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.2  | -8.1 dB |
| Peaking | 152 Hz  | 0.89 | -2.9 dB |
| Peaking | 2246 Hz | 1.64 | -5.9 dB |
| Peaking | 3536 Hz | 4.29 | 5.8 dB  |
| Peaking | 6562 Hz | 7.07 | 4.8 dB  |
| Peaking | 288 Hz  | 2.22 | -0.6 dB |
| Peaking | 725 Hz  | 1.55 | 1.7 dB  |
| Peaking | 1615 Hz | 4.94 | -1.0 dB |
| Peaking | 4935 Hz | 7.41 | -2.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.4 dB |
| Peaking | 62 Hz    | 1.41 | -4.9 dB |
| Peaking | 125 Hz   | 1.41 | -4.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.0 dB |
| Peaking | 4000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monster%20Jamz/Monster%20Jamz.png)