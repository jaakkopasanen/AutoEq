# Sony MDR-7520
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.8; 28 -1.7; 31 -2.8; 34 -3.9; 37 -4.8; 41 -6.0; 45 -7.0; 49 -7.8; 54 -8.8; 60 -9.8; 66 -10.5; 72 -11.0; 79 -11.6; 87 -12.1; 96 -12.6; 106 -12.7; 116 -12.5; 128 -12.2; 141 -11.3; 155 -10.7; 170 -10.1; 187 -8.1; 206 -7.1; 227 -6.3; 249 -5.0; 274 -4.2; 302 -4.7; 332 -3.9; 365 -4.3; 402 -4.8; 442 -5.0; 486 -5.3; 535 -5.2; 588 -4.7; 647 -4.4; 712 -4.6; 783 -4.4; 861 -4.5; 947 -4.7; 1042 -4.9; 1146 -5.2; 1261 -5.8; 1387 -6.9; 1526 -8.3; 1678 -9.8; 1846 -11.0; 2031 -12.9; 2234 -13.3; 2457 -12.1; 2703 -11.1; 2973 -8.9; 3270 -7.1; 3597 -4.0; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -1.9; 6373 -1.1; 7010 -4.0; 7711 -6.4; 8482 -13.1; 9330 -15.8; 10263 -11.9; 11289 -6.6; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-7520 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-7520 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 24 Hz    | 1.56 | 6.7 dB   |
| Peaking | 100 Hz   | 1.08 | -7.1 dB  |
| Peaking | 2248 Hz  | 0.95 | -21.1 dB |
| Peaking | 3172 Hz  | 0.27 | 14.4 dB  |
| Peaking | 9270 Hz  | 2.39 | -16.6 dB |
| Peaking | 160 Hz   | 4.27 | -1.8 dB  |
| Peaking | 276 Hz   | 2.29 | 2.2 dB   |
| Peaking | 3248 Hz  | 3.11 | -4.6 dB  |
| Peaking | 3808 Hz  | 1.87 | 3.4 dB   |
| Peaking | 15298 Hz | 1.37 | -1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | -4.3 dB |
| Peaking | 125 Hz   | 1.41 | -6.6 dB |
| Peaking | 250 Hz   | 1.41 | 2.7 dB  |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -9.2 dB |
| Peaking | 4000 Hz  | 1.41 | 7.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-7520/Sony%20MDR-7520.png)