# JBL Everest 310
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.1; 23 -12.0; 25 -11.9; 28 -11.6; 31 -11.3; 34 -10.9; 37 -10.6; 41 -10.2; 45 -10.0; 49 -10.0; 54 -10.2; 60 -10.3; 66 -10.3; 72 -10.2; 79 -9.9; 87 -9.6; 96 -9.2; 106 -8.6; 116 -8.1; 128 -7.7; 141 -7.0; 155 -6.2; 170 -5.6; 187 -5.5; 206 -4.8; 227 -3.8; 249 -3.3; 274 -3.5; 302 -3.9; 332 -4.5; 365 -5.1; 402 -5.8; 442 -6.3; 486 -7.7; 535 -9.0; 588 -9.4; 647 -9.5; 712 -9.4; 783 -9.3; 861 -9.1; 947 -9.0; 1042 -8.6; 1146 -8.2; 1261 -7.8; 1387 -7.6; 1526 -8.0; 1678 -7.8; 1846 -7.4; 2031 -7.0; 2234 -6.8; 2457 -6.9; 2703 -7.8; 2973 -9.5; 3270 -9.9; 3597 -8.6; 3957 -5.1; 4353 -1.1; 4788 -0.5; 5267 -0.5; 5793 -2.9; 6373 -6.2; 7010 -8.2; 7711 -7.0; 8482 -6.5; 9330 -6.5; 10263 -8.6; 11289 -11.4; 12418 -11.5; 13660 -10.2; 15026 -9.5; 16529 -8.9; 18182 -8.9; 20000 -10.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL Everest 310 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL Everest 310 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 0.9  | -5.5 dB |
| Peaking | 72 Hz    | 1.9  | -3.2 dB |
| Peaking | 2103 Hz  | 0.35 | -2.1 dB |
| Peaking | 4959 Hz  | 2.88 | 8.9 dB  |
| Peaking | 13783 Hz | 0.8  | -4.2 dB |
| Peaking | 277 Hz   | 1.57 | 3.9 dB  |
| Peaking | 647 Hz   | 1.6  | -2.7 dB |
| Peaking | 2564 Hz  | 1.33 | 3.3 dB  |
| Peaking | 3205 Hz  | 2.28 | -5.1 dB |
| Peaking | 4241 Hz  | 7.73 | 2.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.8 dB |
| Peaking | 62 Hz    | 1.41 | -3.0 dB |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | 4.4 dB  |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | -2.1 dB |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB |
| Peaking | 4000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -5.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/JBL%20Everest%20310/JBL%20Everest%20310.png)