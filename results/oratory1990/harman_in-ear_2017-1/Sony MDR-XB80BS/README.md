# Sony MDR-XB80BS
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.5; 23 -8.6; 25 -8.6; 28 -8.6; 31 -8.7; 34 -8.8; 37 -8.9; 41 -9.0; 45 -9.2; 49 -9.4; 54 -9.6; 60 -9.9; 66 -10.2; 72 -10.5; 79 -10.8; 87 -11.2; 96 -11.9; 106 -12.2; 116 -12.3; 128 -12.3; 141 -12.1; 155 -11.8; 170 -11.2; 187 -10.5; 206 -9.7; 227 -8.8; 249 -8.1; 274 -7.5; 302 -7.0; 332 -6.6; 365 -6.4; 402 -6.4; 442 -6.5; 486 -6.5; 535 -6.6; 588 -6.6; 647 -6.6; 712 -6.5; 783 -6.4; 861 -6.3; 947 -6.4; 1042 -6.5; 1146 -6.5; 1261 -6.2; 1387 -5.5; 1526 -4.7; 1678 -4.1; 1846 -3.6; 2031 -3.4; 2234 -3.4; 2457 -3.7; 2703 -3.5; 2973 -2.2; 3270 -0.6; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -2.1; 5793 -5.8; 6373 -4.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.6; 15026 -11.6; 16529 -16.4; 18182 -16.9; 20000 -15.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-XB80BS GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-XB80BS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 47 Hz    |  0.45 | -2.4 dB  |
| Peaking | 128 Hz   |  1.11 | -5.1 dB  |
| Peaking | 1859 Hz  |  3.05 | 1.8 dB   |
| Peaking | 3987 Hz  |  1.17 | 6.5 dB   |
| Peaking | 18354 Hz |  0.87 | -12.0 dB |
| Peaking | 12 Hz    |  1.92 | -1.3 dB  |
| Peaking | 357 Hz   |  2.87 | 0.9 dB   |
| Peaking | 5908 Hz  | 14.08 | -2.9 dB  |
| Peaking | 13622 Hz |  1.98 | 3.3 dB   |
| Peaking | 16036 Hz |  2.72 | -3.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.9 dB |
| Peaking | 62 Hz    | 1.41 | -2.3 dB |
| Peaking | 125 Hz   | 1.41 | -6.0 dB |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -9.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Sony%20MDR-XB80BS/Sony%20MDR-XB80BS.png)