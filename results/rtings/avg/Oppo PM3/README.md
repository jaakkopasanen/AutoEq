# Oppo PM3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.7; 23 -2.5; 25 -2.3; 28 -2.0; 31 -1.7; 34 -1.4; 37 -1.2; 41 -1.1; 45 -1.0; 49 -0.9; 54 -1.1; 60 -1.4; 66 -2.0; 72 -2.6; 79 -3.2; 87 -3.8; 96 -4.3; 106 -4.7; 116 -5.1; 128 -5.4; 141 -5.6; 155 -5.7; 170 -5.5; 187 -5.3; 206 -4.8; 227 -4.3; 249 -3.8; 274 -3.2; 302 -2.6; 332 -2.2; 365 -2.0; 402 -2.2; 442 -2.5; 486 -3.1; 535 -3.6; 588 -4.2; 647 -4.2; 712 -3.8; 783 -3.1; 861 -2.3; 947 -1.5; 1042 -1.3; 1146 -2.3; 1261 -3.2; 1387 -3.7; 1526 -4.2; 1678 -4.6; 1846 -5.6; 2031 -5.5; 2234 -6.2; 2457 -5.8; 2703 -5.7; 2973 -5.4; 3270 -4.9; 3597 -4.5; 3957 -4.0; 4353 -4.5; 4788 -2.9; 5267 -1.1; 5793 -0.5; 6373 -4.5; 7010 -9.3; 7711 -10.5; 8482 -12.1; 9330 -11.8; 10263 -6.2; 11289 -4.5; 12418 -4.5; 13660 -4.5; 15026 -4.5; 16529 -4.5; 18182 -4.5; 20000 -4.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oppo PM3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oppo PM3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 42 Hz    | 1.28 | 4.1 dB  |
| Peaking | 371 Hz   | 2.55 | 2.7 dB  |
| Peaking | 996 Hz   | 3.34 | 3.5 dB  |
| Peaking | 5615 Hz  | 4.3  | 6.3 dB  |
| Peaking | 8306 Hz  | 2.29 | -8.6 dB |
| Peaking | 22 Hz    | 2.19 | 0.9 dB  |
| Peaking | 65 Hz    | 3.63 | 1.1 dB  |
| Peaking | 144 Hz   | 1.98 | -1.7 dB |
| Peaking | 2301 Hz  | 2.69 | -1.7 dB |
| Peaking | 11213 Hz | 5.49 | 2.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB  |
| Peaking | 62 Hz    | 1.41 | 2.9 dB  |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | 1.2 dB  |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.7 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Oppo%20PM3/Oppo%20PM3.png)