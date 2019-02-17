# Monster Lil Jamz
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.1; 23 -15.1; 25 -15.0; 28 -14.8; 31 -14.7; 34 -14.5; 37 -14.4; 41 -14.2; 45 -14.1; 49 -13.9; 54 -13.8; 60 -13.7; 66 -13.6; 72 -13.5; 79 -13.4; 87 -13.3; 96 -13.2; 106 -12.9; 116 -12.8; 128 -12.6; 141 -12.4; 155 -12.3; 170 -12.0; 187 -11.7; 206 -11.4; 227 -11.0; 249 -10.6; 274 -10.2; 302 -9.7; 332 -9.2; 365 -8.7; 402 -8.3; 442 -7.9; 486 -7.4; 535 -6.9; 588 -6.3; 647 -5.9; 712 -5.5; 783 -5.4; 861 -5.3; 947 -5.6; 1042 -6.0; 1146 -6.6; 1261 -7.1; 1387 -6.8; 1526 -7.9; 1678 -8.6; 1846 -9.0; 2031 -9.2; 2234 -9.5; 2457 -9.3; 2703 -7.9; 2973 -5.3; 3270 -2.4; 3597 -0.5; 3957 -1.1; 4353 -3.4; 4788 -5.0; 5267 -5.1; 5793 -3.5; 6373 -0.8; 7010 -3.3; 7711 -5.5; 8482 -5.8; 9330 -5.8; 10263 -5.8; 11289 -5.8; 12418 -5.8; 13660 -5.8; 15026 -7.0; 16529 -5.8; 18182 -5.8; 20000 -5.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Lil Jamz GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Lil Jamz ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 0.14 | -9.0 dB |
| Peaking | 198 Hz   | 0.86 | -2.9 dB |
| Peaking | 2253 Hz  | 1.67 | -4.6 dB |
| Peaking | 3608 Hz  | 3.1  | 6.9 dB  |
| Peaking | 6489 Hz  | 6.17 | 5.2 dB  |
| Peaking | 378 Hz   | 2.03 | -0.5 dB |
| Peaking | 775 Hz   | 2.01 | 1.4 dB  |
| Peaking | 1624 Hz  | 5.81 | -0.9 dB |
| Peaking | 15024 Hz | 4.66 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.4 dB |
| Peaking | 62 Hz    | 1.41 | -5.5 dB |
| Peaking | 125 Hz   | 1.41 | -5.5 dB |
| Peaking | 250 Hz   | 1.41 | -4.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.0 dB |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Monster%20Lil%20Jamz/Monster%20Lil%20Jamz.png)