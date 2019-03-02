# JBL Everest 310
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.4; 23 -12.2; 25 -12.1; 28 -11.8; 31 -11.5; 34 -11.1; 37 -10.7; 41 -10.3; 45 -10.2; 49 -10.2; 54 -10.3; 60 -10.4; 66 -10.5; 72 -10.4; 79 -10.1; 87 -9.8; 96 -9.5; 106 -8.9; 116 -8.4; 128 -7.8; 141 -7.2; 155 -6.4; 170 -5.8; 187 -5.7; 206 -4.9; 227 -3.9; 249 -3.3; 274 -3.6; 302 -4.0; 332 -4.6; 365 -5.2; 402 -5.9; 442 -6.4; 486 -7.6; 535 -8.9; 588 -9.3; 647 -9.3; 712 -9.2; 783 -9.1; 861 -9.0; 947 -8.8; 1042 -8.5; 1146 -8.0; 1261 -7.7; 1387 -7.5; 1526 -7.7; 1678 -7.5; 1846 -7.0; 2031 -6.5; 2234 -5.9; 2457 -5.9; 2703 -7.2; 2973 -9.4; 3270 -10.1; 3597 -8.9; 3957 -5.5; 4353 -1.4; 4788 -0.5; 5267 -0.5; 5793 -2.9; 6373 -7.2; 7010 -8.3; 7711 -6.4; 8482 -6.5; 9330 -7.5; 10263 -9.1; 11289 -10.3; 12418 -11.2; 13660 -11.0; 15026 -9.9; 16529 -9.1; 18182 -9.0; 20000 -11.0
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
| Peaking | 24 Hz    | 0.86 | -5.7 dB |
| Peaking | 73 Hz    | 1.85 | -3.3 dB |
| Peaking | 1972 Hz  | 0.34 | -1.6 dB |
| Peaking | 4986 Hz  | 3.05 | 8.9 dB  |
| Peaking | 16098 Hz | 0.34 | -3.7 dB |
| Peaking | 276 Hz   | 1.64 | 3.8 dB  |
| Peaking | 653 Hz   | 1.56 | -2.5 dB |
| Peaking | 2508 Hz  | 1.72 | 3.8 dB  |
| Peaking | 3184 Hz  | 2.54 | -5.3 dB |
| Peaking | 4277 Hz  | 7.88 | 2.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.0 dB |
| Peaking | 62 Hz    | 1.41 | -3.2 dB |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | 4.3 dB  |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | -2.1 dB |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB |
| Peaking | 4000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -5.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/JBL%20Everest%20310/JBL%20Everest%20310.png)