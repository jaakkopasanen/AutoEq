# Sony WH-CH700N
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.7; 23 -7.9; 25 -8.1; 28 -8.3; 31 -8.3; 34 -8.2; 37 -8.0; 41 -7.6; 45 -7.2; 49 -6.8; 54 -6.2; 60 -5.7; 66 -5.5; 72 -5.4; 79 -5.4; 87 -5.5; 96 -5.6; 106 -5.9; 116 -6.3; 128 -6.5; 141 -6.6; 155 -6.4; 170 -6.1; 187 -5.7; 206 -5.6; 227 -5.6; 249 -5.5; 274 -5.2; 302 -4.9; 332 -4.5; 365 -3.9; 402 -3.3; 442 -3.0; 486 -2.5; 535 -1.9; 588 -1.7; 647 -1.6; 712 -1.8; 783 -2.0; 861 -1.9; 947 -1.5; 1042 -0.8; 1146 -0.5; 1261 -0.9; 1387 -1.7; 1526 -3.0; 1678 -5.1; 1846 -7.3; 2031 -8.6; 2234 -7.2; 2457 -6.5; 2703 -7.0; 2973 -8.7; 3270 -10.3; 3597 -9.8; 3957 -5.8; 4353 -1.0; 4788 -7.9; 5267 -14.9; 5793 -9.8; 6373 -5.8; 7010 -3.3; 7711 -4.7; 8482 -5.2; 9330 -6.2; 10263 -5.7; 11289 -5.3; 12418 -5.3; 13660 -5.0; 15026 -5.0; 16529 -7.0; 18182 -12.8; 20000 -5.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WH-CH700N GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WH-CH700N ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 577 Hz   | 2.05 | 2.9 dB   |
| Peaking | 1204 Hz  | 1.34 | 5.2 dB   |
| Peaking | 1937 Hz  | 4.4  | -3.3 dB  |
| Peaking | 3422 Hz  | 0.7  | -3.5 dB  |
| Peaking | 18354 Hz | 2.07 | -8.8 dB  |
| Peaking | 3443 Hz  | 5.51 | -3.7 dB  |
| Peaking | 4415 Hz  | 4.74 | 10.3 dB  |
| Peaking | 5210 Hz  | 4.63 | -11.0 dB |
| Peaking | 6942 Hz  | 3.93 | 3.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.0 dB |
| Peaking | 62 Hz    | 1.41 | 0.4 dB  |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.4 dB |
| Peaking | 4000 Hz  | 1.41 | -3.1 dB |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -2.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20WH-CH700N/Sony%20WH-CH700N.png)