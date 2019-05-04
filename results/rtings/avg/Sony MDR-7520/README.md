# Sony MDR-7520
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.1; 23 -3.7; 25 -4.2; 28 -4.9; 31 -5.5; 34 -6.0; 37 -6.4; 41 -6.8; 45 -7.2; 49 -7.5; 54 -7.9; 60 -8.4; 66 -8.8; 72 -9.2; 79 -9.7; 87 -10.1; 96 -10.5; 106 -10.7; 116 -10.9; 128 -10.9; 141 -10.6; 155 -9.9; 170 -9.3; 187 -8.6; 206 -7.5; 227 -6.0; 249 -4.9; 274 -5.4; 302 -3.3; 332 -2.4; 365 -3.0; 402 -4.1; 442 -5.0; 486 -5.6; 535 -5.6; 588 -5.4; 647 -5.1; 712 -4.8; 783 -4.6; 861 -4.1; 947 -3.9; 1042 -3.9; 1146 -4.3; 1261 -4.9; 1387 -5.6; 1526 -6.6; 1678 -7.7; 1846 -9.1; 2031 -9.9; 2234 -10.0; 2457 -10.2; 2703 -11.2; 2973 -11.3; 3270 -9.1; 3597 -5.9; 3957 -1.2; 4353 -0.5; 4788 -0.5; 5267 -3.6; 5793 -4.8; 6373 -1.4; 7010 -4.0; 7711 -9.3; 8482 -14.3; 9330 -15.1; 10263 -12.9; 11289 -8.0; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -9.6; 18182 -8.3; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-7520 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-7520 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 106 Hz   | 0.65 | -8.6 dB  |
| Peaking | 163 Hz   | 0.1  | 4.0 dB   |
| Peaking | 2979 Hz  | 1.03 | -14.7 dB |
| Peaking | 4178 Hz  | 0.97 | 14.4 dB  |
| Peaking | 9141 Hz  | 2.77 | -11.7 dB |
| Peaking | 20 Hz    | 3.13 | 1.8 dB   |
| Peaking | 332 Hz   | 4.15 | 2.9 dB   |
| Peaking | 522 Hz   | 2.78 | -2.0 dB  |
| Peaking | 12700 Hz | 2.99 | 1.2 dB   |
| Peaking | 17064 Hz | 2.4  | -3.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.0 dB  |
| Peaking | 62 Hz    | 1.41 | -1.9 dB |
| Peaking | 125 Hz   | 1.41 | -5.4 dB |
| Peaking | 250 Hz   | 1.41 | 2.5 dB  |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.1 dB |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.2 dB |
| Peaking | 16000 Hz | 1.41 | -1.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20MDR-7520/Sony%20MDR-7520.png)