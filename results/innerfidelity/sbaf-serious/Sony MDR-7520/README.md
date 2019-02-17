# Sony MDR-7520
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.6; 25 -2.6; 28 -3.9; 31 -5.1; 34 -6.1; 37 -7.1; 41 -8.2; 45 -9.2; 49 -10.1; 54 -11.0; 60 -12.0; 66 -12.7; 72 -13.2; 79 -13.8; 87 -14.3; 96 -14.9; 106 -14.9; 116 -14.8; 128 -14.4; 141 -13.6; 155 -12.9; 170 -12.3; 187 -10.3; 206 -9.3; 227 -8.5; 249 -7.2; 274 -6.4; 302 -6.9; 332 -6.1; 365 -6.6; 402 -7.0; 442 -7.2; 486 -7.5; 535 -7.4; 588 -6.9; 647 -6.7; 712 -6.8; 783 -6.6; 861 -6.7; 947 -6.9; 1042 -7.1; 1146 -7.4; 1261 -8.0; 1387 -9.1; 1526 -10.5; 1678 -12.0; 1846 -13.3; 2031 -15.1; 2234 -15.5; 2457 -14.3; 2703 -13.3; 2973 -11.1; 3270 -9.3; 3597 -6.2; 3957 -1.6; 4353 -1.0; 4788 -1.0; 5267 -1.7; 5793 -4.2; 6373 -2.6; 7010 -4.5; 7711 -7.7; 8482 -15.3; 9330 -18.1; 10263 -14.2; 11289 -7.5; 12418 -7.0; 13660 -7.0; 15026 -7.0; 16529 -7.0; 18182 -7.0; 20000 -7.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-7520 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-7520 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 22 Hz   | 1.83 | 7.1 dB   |
| Peaking | 98 Hz   | 0.97 | -8.6 dB  |
| Peaking | 2383 Hz | 1.48 | -11.6 dB |
| Peaking | 4780 Hz | 0.92 | 8.6 dB   |
| Peaking | 9185 Hz | 3.32 | -14.7 dB |
| Peaking | 162 Hz  | 3.68 | -2.0 dB  |
| Peaking | 284 Hz  | 1.95 | 1.9 dB   |
| Peaking | 1725 Hz | 0.77 | 3.4 dB   |
| Peaking | 1757 Hz | 1.74 | -4.5 dB  |
| Peaking | 3223 Hz | 5.34 | -2.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB   |
| Peaking | 62 Hz    | 1.41 | -5.6 dB  |
| Peaking | 125 Hz   | 1.41 | -7.9 dB  |
| Peaking | 250 Hz   | 1.41 | 1.4 dB   |
| Peaking | 500 Hz   | 1.41 | -0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.8 dB   |
| Peaking | 2000 Hz  | 1.41 | -11.0 dB |
| Peaking | 4000 Hz  | 1.41 | 7.6 dB   |
| Peaking | 8000 Hz  | 1.41 | -4.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-7520/Sony%20MDR-7520.png)