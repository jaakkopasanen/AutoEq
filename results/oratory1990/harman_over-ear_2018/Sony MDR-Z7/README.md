# Sony MDR-Z7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.8; 23 -1.8; 25 -2.7; 28 -3.9; 31 -4.8; 34 -5.5; 37 -6.0; 41 -6.3; 45 -6.4; 49 -6.4; 54 -6.5; 60 -6.7; 66 -6.9; 72 -7.1; 79 -7.2; 87 -7.6; 96 -7.9; 106 -8.2; 116 -8.3; 128 -8.4; 141 -8.5; 155 -8.7; 170 -8.7; 187 -8.3; 206 -7.6; 227 -6.8; 249 -6.1; 274 -5.6; 302 -5.3; 332 -5.0; 365 -4.8; 402 -4.6; 442 -4.7; 486 -5.0; 535 -5.2; 588 -5.5; 647 -6.1; 712 -6.9; 783 -7.5; 861 -7.7; 947 -7.1; 1042 -6.0; 1146 -4.6; 1261 -3.2; 1387 -2.8; 1526 -3.6; 1678 -4.9; 1846 -6.0; 2031 -6.8; 2234 -7.6; 2457 -8.6; 2703 -8.5; 2973 -6.6; 3270 -3.6; 3597 -0.7; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -2.6; 6373 -6.1; 7010 -9.7; 7711 -12.9; 8482 -14.1; 9330 -12.8; 10263 -9.5; 11289 -6.6; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.8; 20000 -15.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-Z7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-Z7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 2.04 | 5.8 dB  |
| Peaking | 134 Hz   | 1.67 | -2.4 dB |
| Peaking | 1355 Hz  | 4.55 | 4.1 dB  |
| Peaking | 4763 Hz  | 1.88 | 8.0 dB  |
| Peaking | 8302 Hz  | 2.38 | -9.4 dB |
| Peaking | 410 Hz   | 1.55 | 2.1 dB  |
| Peaking | 824 Hz   | 4.36 | -1.9 dB |
| Peaking | 2606 Hz  | 3.41 | -3.8 dB |
| Peaking | 3559 Hz  | 6.06 | 3.5 dB  |
| Peaking | 11460 Hz | 5.52 | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.5 dB  |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | 0.5 dB  |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 7.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sony%20MDR-Z7/Sony%20MDR-Z7.png)