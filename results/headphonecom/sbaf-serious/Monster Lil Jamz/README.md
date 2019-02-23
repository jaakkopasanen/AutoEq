# Monster Lil Jamz
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.9; 23 -14.8; 25 -14.7; 28 -14.6; 31 -14.4; 34 -14.3; 37 -14.1; 41 -13.9; 45 -13.8; 49 -13.7; 54 -13.5; 60 -13.4; 66 -13.4; 72 -13.3; 79 -13.2; 87 -13.1; 96 -12.9; 106 -12.7; 116 -12.5; 128 -12.3; 141 -12.2; 155 -12.0; 170 -11.8; 187 -11.5; 206 -11.1; 227 -10.8; 249 -10.4; 274 -10.0; 302 -9.5; 332 -8.9; 365 -8.5; 402 -8.1; 442 -7.6; 486 -7.1; 535 -6.6; 588 -6.1; 647 -5.7; 712 -5.3; 783 -5.1; 861 -5.0; 947 -5.4; 1042 -5.8; 1146 -6.3; 1261 -6.8; 1387 -6.5; 1526 -7.7; 1678 -8.4; 1846 -8.7; 2031 -9.0; 2234 -9.2; 2457 -9.0; 2703 -7.6; 2973 -5.1; 3270 -2.1; 3597 -0.5; 3957 -0.9; 4353 -3.1; 4788 -4.8; 5267 -4.9; 5793 -3.3; 6373 -1.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.7; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Lil Jamz GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Lil Jamz ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.18 | -8.1 dB |
| Peaking | 178 Hz  | 0.98 | -2.7 dB |
| Peaking | 2307 Hz | 2.19 | -4.1 dB |
| Peaking | 3628 Hz | 2.72 | 7.1 dB  |
| Peaking | 6422 Hz | 5.7  | 5.3 dB  |
| Peaking | 93 Hz   | 3.87 | -0.4 dB |
| Peaking | 322 Hz  | 2.04 | -0.7 dB |
| Peaking | 784 Hz  | 1.56 | 2.0 dB  |
| Peaking | 1677 Hz | 4.89 | -1.2 dB |
| Peaking | 8044 Hz | 4.37 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.4 dB |
| Peaking | 62 Hz    | 1.41 | -4.9 dB |
| Peaking | 125 Hz   | 1.41 | -4.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.3 dB |
| Peaking | 4000 Hz  | 1.41 | 5.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Monster%20Lil%20Jamz/Monster%20Lil%20Jamz.png)