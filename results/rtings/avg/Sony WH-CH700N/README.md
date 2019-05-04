# Sony WH-CH700N
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.3; 23 -7.5; 25 -7.7; 28 -7.9; 31 -8.0; 34 -7.9; 37 -7.7; 41 -7.3; 45 -6.9; 49 -6.4; 54 -5.9; 60 -5.3; 66 -5.1; 72 -5.0; 79 -5.0; 87 -5.1; 96 -5.3; 106 -5.6; 116 -5.9; 128 -6.2; 141 -6.2; 155 -6.1; 170 -5.7; 187 -5.4; 206 -5.2; 227 -5.3; 249 -5.1; 274 -4.9; 302 -4.6; 332 -4.2; 365 -3.6; 402 -3.1; 442 -2.7; 486 -2.3; 535 -1.8; 588 -1.5; 647 -1.5; 712 -1.7; 783 -2.0; 861 -1.8; 947 -1.4; 1042 -0.7; 1146 -0.5; 1261 -1.0; 1387 -1.7; 1526 -3.2; 1678 -5.2; 1846 -7.5; 2031 -8.8; 2234 -7.8; 2457 -7.1; 2703 -7.4; 2973 -8.7; 3270 -10.0; 3597 -9.3; 3957 -5.0; 4353 -0.7; 4788 -8.2; 5267 -14.8; 5793 -9.5; 6373 -4.7; 7010 -2.9; 7711 -4.5; 8482 -4.8; 9330 -4.8; 10263 -5.0; 11289 -6.0; 12418 -5.3; 13660 -4.8; 15026 -4.8; 16529 -6.9; 18182 -12.7; 20000 -4.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WH-CH700N GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WH-CH700N ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 1980 Hz  | 0.46 | 8.7 dB   |
| Peaking | 2046 Hz  | 1.65 | -12.0 dB |
| Peaking | 3248 Hz  | 3.46 | -8.9 dB  |
| Peaking | 5307 Hz  | 6.43 | -13.5 dB |
| Peaking | 18250 Hz | 1.77 | -8.7 dB  |
| Peaking | 29 Hz    | 1.2  | -3.5 dB  |
| Peaking | 143 Hz   | 2.35 | -1.6 dB  |
| Peaking | 247 Hz   | 3.52 | -0.8 dB  |
| Peaking | 4349 Hz  | 7.63 | 8.2 dB   |
| Peaking | 4435 Hz  | 2.64 | -3.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.8 dB |
| Peaking | 62 Hz    | 1.41 | 0.6 dB  |
| Peaking | 125 Hz   | 1.41 | -1.2 dB |
| Peaking | 250 Hz   | 1.41 | -0.7 dB |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.1 dB |
| Peaking | 4000 Hz  | 1.41 | -2.9 dB |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -2.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20WH-CH700N/Sony%20WH-CH700N.png)