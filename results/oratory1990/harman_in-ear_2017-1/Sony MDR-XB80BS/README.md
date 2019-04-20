# Sony MDR-XB80BS
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.3; 23 -9.3; 25 -9.4; 28 -9.4; 31 -9.5; 34 -9.6; 37 -9.7; 41 -9.8; 45 -10.0; 49 -10.2; 54 -10.4; 60 -10.7; 66 -11.0; 72 -11.3; 79 -11.6; 87 -12.0; 96 -12.7; 106 -13.0; 116 -13.1; 128 -13.1; 141 -12.9; 155 -12.5; 170 -12.0; 187 -11.3; 206 -10.5; 227 -9.6; 249 -8.9; 274 -8.3; 302 -7.8; 332 -7.4; 365 -7.2; 402 -7.2; 442 -7.3; 486 -7.3; 535 -7.4; 588 -7.4; 647 -7.4; 712 -7.3; 783 -7.2; 861 -7.1; 947 -7.2; 1042 -7.3; 1146 -7.3; 1261 -7.0; 1387 -6.2; 1526 -5.5; 1678 -4.9; 1846 -4.4; 2031 -4.2; 2234 -4.2; 2457 -4.5; 2703 -4.3; 2973 -3.0; 3270 -1.2; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.6; 5267 -3.0; 5793 -6.5; 6373 -4.8; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.9; 15026 -12.5; 16529 -17.4; 18182 -17.8; 20000 -16.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-XB80BS GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-XB80BS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 15 Hz    |  0.59 | -2.2 dB  |
| Peaking | 69 Hz    |  0.52 | -2.6 dB  |
| Peaking | 133 Hz   |  0.94 | -5.0 dB  |
| Peaking | 3961 Hz  |  1.28 | 6.5 dB   |
| Peaking | 18314 Hz |  0.88 | -13.1 dB |
| Peaking | 1209 Hz  |  1.08 | -1.3 dB  |
| Peaking | 1738 Hz  |  2.55 | 1.9 dB   |
| Peaking | 5851 Hz  | 12    | -3.2 dB  |
| Peaking | 13489 Hz |  1.6  | 3.6 dB   |
| Peaking | 15826 Hz |  2.51 | -4.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.7 dB  |
| Peaking | 62 Hz    | 1.41 | -2.9 dB  |
| Peaking | 125 Hz   | 1.41 | -6.6 dB  |
| Peaking | 250 Hz   | 1.41 | -1.2 dB  |
| Peaking | 500 Hz   | 1.41 | -0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB   |
| Peaking | 16000 Hz | 1.41 | -10.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Sony%20MDR-XB80BS/Sony%20MDR-XB80BS.png)