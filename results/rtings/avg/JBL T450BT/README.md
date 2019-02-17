# JBL T450BT
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.1; 23 -4.6; 25 -5.1; 28 -5.8; 31 -6.3; 34 -6.8; 37 -7.2; 41 -7.6; 45 -7.9; 49 -8.1; 54 -8.4; 60 -8.8; 66 -9.4; 72 -9.9; 79 -10.3; 87 -10.7; 96 -11.0; 106 -11.3; 116 -11.5; 128 -11.5; 141 -11.5; 155 -11.4; 170 -11.3; 187 -11.0; 206 -10.5; 227 -9.8; 249 -9.0; 274 -8.1; 302 -7.2; 332 -7.3; 365 -6.7; 402 -5.8; 442 -5.9; 486 -6.2; 535 -6.4; 588 -6.5; 647 -6.6; 712 -6.7; 783 -6.7; 861 -6.7; 947 -6.6; 1042 -6.4; 1146 -6.1; 1261 -6.0; 1387 -6.1; 1526 -6.0; 1678 -5.8; 1846 -5.4; 2031 -5.2; 2234 -4.1; 2457 -4.3; 2703 -4.9; 2973 -6.0; 3270 -6.8; 3597 -6.0; 3957 -4.6; 4353 -3.6; 4788 -1.8; 5267 -0.5; 5793 -0.9; 6373 -3.0; 7010 -5.8; 7711 -9.7; 8482 -12.1; 9330 -13.1; 10263 -11.5; 11289 -9.3; 12418 -8.1; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL T450BT GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL T450BT ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 2.17 | 2.6 dB  |
| Peaking | 100 Hz   | 0.94 | -4.4 dB |
| Peaking | 179 Hz   | 1.85 | -3.1 dB |
| Peaking | 5608 Hz  | 1.77 | 7.6 dB  |
| Peaking | 8957 Hz  | 1.84 | -8.4 dB |
| Peaking | 20 Hz    | 1.48 | 0.6 dB  |
| Peaking | 421 Hz   | 4.2  | 1.3 dB  |
| Peaking | 2386 Hz  | 2.37 | 2.2 dB  |
| Peaking | 3274 Hz  | 3.89 | -2.1 dB |
| Peaking | 13960 Hz | 4.03 | 0.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.1 dB  |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | -5.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/JBL%20T450BT/JBL%20T450BT.png)