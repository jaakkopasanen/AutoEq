# Sony WH-1000XM2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.9; 23 -9.5; 25 -9.2; 28 -8.9; 31 -8.6; 34 -8.4; 37 -8.1; 41 -7.8; 45 -7.6; 49 -7.6; 54 -7.6; 60 -7.7; 66 -7.9; 72 -8.0; 79 -8.2; 87 -8.5; 96 -8.7; 106 -8.9; 116 -9.1; 128 -9.3; 141 -9.4; 155 -9.3; 170 -9.2; 187 -9.0; 206 -8.5; 227 -8.0; 249 -7.8; 274 -7.5; 302 -7.1; 332 -6.7; 365 -6.3; 402 -5.9; 442 -5.5; 486 -5.2; 535 -4.8; 588 -4.3; 647 -3.7; 712 -3.1; 783 -1.0; 861 -0.5; 947 -0.5; 1042 -0.6; 1146 -2.2; 1261 -4.5; 1387 -7.3; 1526 -8.9; 1678 -10.3; 1846 -11.7; 2031 -11.2; 2234 -8.8; 2457 -7.5; 2703 -7.7; 2973 -7.0; 3270 -6.9; 3597 -7.8; 3957 -8.8; 4353 -7.0; 4788 -4.8; 5267 -7.0; 5793 -7.8; 6373 -3.9; 7010 -4.7; 7711 -6.5; 8482 -7.0; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -7.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WH-1000XM2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WH-1000XM2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 0.93 | -3.4 dB |
| Peaking | 143 Hz   | 0.84 | -3.0 dB |
| Peaking | 963 Hz   | 1.29 | 7.6 dB  |
| Peaking | 1754 Hz  | 1.77 | -7.0 dB |
| Peaking | 6614 Hz  | 8.93 | 3.2 dB  |
| Peaking | 4044 Hz  | 3.88 | -4.8 dB |
| Peaking | 4761 Hz  | 1.81 | 4.2 dB  |
| Peaking | 5548 Hz  | 6.51 | -4.9 dB |
| Peaking | 8184 Hz  | 7.16 | -1.3 dB |
| Peaking | 10472 Hz | 1.9  | -0.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.4 dB |
| Peaking | 62 Hz    | 1.41 | -0.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 6.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.8 dB |
| Peaking | 4000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20WH-1000XM2/Sony%20WH-1000XM2.png)