# Bowers & Wilkins PX
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.7; 23 -10.0; 25 -10.2; 28 -10.5; 31 -10.7; 34 -10.9; 37 -10.9; 41 -10.9; 45 -10.9; 49 -10.9; 54 -10.9; 60 -11.0; 66 -11.2; 72 -11.5; 79 -11.9; 87 -12.4; 96 -13.0; 106 -13.5; 116 -13.9; 128 -14.2; 141 -14.2; 155 -14.2; 170 -14.2; 187 -14.3; 206 -14.7; 227 -15.4; 249 -15.9; 274 -16.2; 302 -15.9; 332 -15.3; 365 -14.3; 402 -13.3; 442 -12.5; 486 -11.8; 535 -11.0; 588 -10.2; 647 -9.3; 712 -8.3; 783 -7.2; 861 -6.3; 947 -5.9; 1042 -6.1; 1146 -6.9; 1261 -7.4; 1387 -7.3; 1526 -7.5; 1678 -8.1; 1846 -8.5; 2031 -9.2; 2234 -9.5; 2457 -9.5; 2703 -7.5; 2973 -2.8; 3270 -0.5; 3597 -11.1; 3957 -11.0; 4353 -10.2; 4788 -8.5; 5267 -5.6; 5793 -4.4; 6373 -6.1; 7010 -7.1; 7711 -7.0; 8482 -9.3; 9330 -9.4; 10263 -5.9; 11289 -5.9; 12418 -6.5; 13660 -12.2; 15026 -9.8; 16529 -5.9; 18182 -5.9; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bowers & Wilkins PX GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers & Wilkins PX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 0.52 | -4.3 dB |
| Peaking | 118 Hz   | 0.93 | -4.7 dB |
| Peaking | 295 Hz   | 0.82 | -9.0 dB |
| Peaking | 4050 Hz  | 4.96 | -5.7 dB |
| Peaking | 14033 Hz | 3.35 | -7.0 dB |
| Peaking | 935 Hz   | 2.98 | 2.2 dB  |
| Peaking | 2689 Hz  | 1.07 | -4.5 dB |
| Peaking | 3137 Hz  | 6.11 | 11.5 dB |
| Peaking | 5630 Hz  | 6.09 | 3.2 dB  |
| Peaking | 8851 Hz  | 6.88 | -4.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.6 dB |
| Peaking | 62 Hz    | 1.41 | -3.4 dB |
| Peaking | 125 Hz   | 1.41 | -6.0 dB |
| Peaking | 250 Hz   | 1.41 | -9.0 dB |
| Peaking | 500 Hz   | 1.41 | -4.5 dB |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.6 dB |
| Peaking | 4000 Hz  | 1.41 | -1.1 dB |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB |
| Peaking | 16000 Hz | 1.41 | -3.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bowers%20&%20Wilkins%20PX/Bowers%20&%20Wilkins%20PX.png)