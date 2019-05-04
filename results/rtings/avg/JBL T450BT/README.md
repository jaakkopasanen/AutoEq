# JBL T450BT
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.4; 23 -3.9; 25 -4.4; 28 -5.0; 31 -5.6; 34 -6.1; 37 -6.5; 41 -6.9; 45 -7.2; 49 -7.4; 54 -7.7; 60 -8.1; 66 -8.7; 72 -9.2; 79 -9.6; 87 -9.9; 96 -10.2; 106 -10.5; 116 -10.7; 128 -10.8; 141 -10.8; 155 -10.7; 170 -10.6; 187 -10.2; 206 -9.8; 227 -9.1; 249 -8.4; 274 -7.5; 302 -6.6; 332 -6.7; 365 -6.1; 402 -5.2; 442 -5.3; 486 -5.7; 535 -6.0; 588 -6.2; 647 -6.4; 712 -6.4; 783 -6.3; 861 -6.2; 947 -6.1; 1042 -6.0; 1146 -5.6; 1261 -5.5; 1387 -5.7; 1526 -5.7; 1678 -5.5; 1846 -5.2; 2031 -5.0; 2234 -4.4; 2457 -4.6; 2703 -4.9; 2973 -5.7; 3270 -6.0; 3597 -5.2; 3957 -3.5; 4353 -2.6; 4788 -1.5; 5267 -0.5; 5793 -0.5; 6373 -1.6; 7010 -5.6; 7711 -9.9; 8482 -10.8; 9330 -10.6; 10263 -10.4; 11289 -9.7; 12418 -7.6; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL T450BT GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL T450BT ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 1.6  | 3.4 dB  |
| Peaking | 129 Hz  | 0.76 | -5.2 dB |
| Peaking | 2373 Hz | 0.06 | 1.0 dB  |
| Peaking | 5885 Hz | 1.63 | 10.2 dB |
| Peaking | 8286 Hz | 1.11 | -9.0 dB |
| Peaking | 210 Hz  | 3.92 | -0.9 dB |
| Peaking | 420 Hz  | 1.92 | 1.6 dB  |
| Peaking | 676 Hz  | 1.01 | -0.9 dB |
| Peaking | 3053 Hz | 1.46 | 1.9 dB  |
| Peaking | 3211 Hz | 3.27 | -3.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.9 dB  |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | 1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/JBL%20T450BT/JBL%20T450BT.png)