# Monster Jamz
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.7; 23 -1.3; 25 -1.8; 28 -2.5; 31 -3.1; 34 -3.6; 37 -4.1; 41 -4.6; 45 -5.1; 49 -5.6; 54 -6.2; 60 -6.8; 66 -7.5; 72 -8.0; 79 -8.6; 87 -9.2; 96 -9.7; 106 -10.2; 116 -10.7; 128 -11.2; 141 -11.6; 155 -12.1; 170 -12.3; 187 -12.6; 206 -12.7; 227 -12.5; 249 -12.3; 274 -12.4; 302 -12.4; 332 -12.0; 365 -11.5; 402 -11.0; 442 -10.5; 486 -9.9; 535 -9.2; 588 -8.6; 647 -7.9; 712 -7.3; 783 -6.8; 861 -6.6; 947 -6.6; 1042 -6.5; 1146 -6.5; 1261 -6.6; 1387 -6.6; 1526 -6.9; 1678 -6.7; 1846 -6.4; 2031 -6.0; 2234 -5.1; 2457 -3.8; 2703 -2.4; 2973 -0.9; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.5; 4788 -1.4; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Jamz GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Jamz ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 0.58 | 6.6 dB  |
| Peaking | 166 Hz  | 0.63 | -5.4 dB |
| Peaking | 341 Hz  | 1.22 | -2.8 dB |
| Peaking | 3418 Hz | 1.83 | 6.2 dB  |
| Peaking | 5681 Hz | 2.78 | 5.5 dB  |
| Peaking | 887 Hz  | 2.63 | 0.8 dB  |
| Peaking | 1777 Hz | 2.01 | -0.9 dB |
| Peaking | 2734 Hz | 5    | 0.9 dB  |
| Peaking | 6570 Hz | 7.34 | 2.1 dB  |
| Peaking | 7785 Hz | 2.25 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.7 dB  |
| Peaking | 62 Hz    | 1.41 | -0.7 dB |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | -5.8 dB |
| Peaking | 500 Hz   | 1.41 | -2.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB |
| Peaking | 4000 Hz  | 1.41 | 7.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Monster%20Jamz/Monster%20Jamz.png)