# Bowers & Wilkins PX
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.0; 23 -6.3; 25 -6.5; 28 -6.8; 31 -7.0; 34 -7.1; 37 -7.2; 41 -7.2; 45 -7.2; 49 -7.2; 54 -7.2; 60 -7.3; 66 -7.5; 72 -7.8; 79 -8.2; 87 -8.7; 96 -9.2; 106 -9.7; 116 -10.1; 128 -10.4; 141 -10.5; 155 -10.5; 170 -10.5; 187 -10.6; 206 -11.0; 227 -11.7; 249 -12.3; 274 -12.6; 302 -12.3; 332 -11.7; 365 -10.8; 402 -9.8; 442 -8.9; 486 -8.3; 535 -7.6; 588 -6.8; 647 -5.9; 712 -4.9; 783 -3.9; 861 -2.9; 947 -2.4; 1042 -2.7; 1146 -3.5; 1261 -4.0; 1387 -4.0; 1526 -4.3; 1678 -4.8; 1846 -5.3; 2031 -6.2; 2234 -6.9; 2457 -6.9; 2703 -4.6; 2973 -0.6; 3270 -0.5; 3597 -7.0; 3957 -7.2; 4353 -6.2; 4788 -5.4; 5267 -2.4; 5793 -0.8; 6373 -1.7; 7010 -4.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.0; 15026 -6.6; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bowers & Wilkins PX GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers & Wilkins PX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 120 Hz   | 1.21 | -2.7 dB |
| Peaking | 290 Hz   | 0.93 | -6.9 dB |
| Peaking | 868 Hz   | 0.2  | 1.7 dB  |
| Peaking | 935 Hz   | 2.05 | 3.4 dB  |
| Peaking | 5921 Hz  | 4.28 | 5.8 dB  |
| Peaking | 38 Hz    | 2.63 | -0.4 dB |
| Peaking | 2413 Hz  | 3.24 | -3.8 dB |
| Peaking | 3225 Hz  | 3.05 | 8.8 dB  |
| Peaking | 3704 Hz  | 4.11 | -7.1 dB |
| Peaking | 13904 Hz | 5.26 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.2 dB |
| Peaking | 62 Hz    | 1.41 | -0.3 dB |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -5.7 dB |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB |
| Peaking | 4000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bowers%20&%20Wilkins%20PX/Bowers%20&%20Wilkins%20PX.png)