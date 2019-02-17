# Howard Leight Sync
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -1.0; 66 -3.1; 72 -5.0; 79 -6.5; 87 -7.8; 96 -10.1; 106 -12.5; 116 -14.7; 128 -16.5; 141 -17.1; 155 -18.0; 170 -17.5; 187 -18.0; 206 -17.4; 227 -16.9; 249 -16.5; 274 -15.9; 302 -15.1; 332 -13.6; 365 -12.9; 402 -12.6; 442 -11.5; 486 -11.7; 535 -11.4; 588 -10.9; 647 -10.7; 712 -10.1; 783 -9.3; 861 -8.3; 947 -7.0; 1042 -6.5; 1146 -6.4; 1261 -6.3; 1387 -6.7; 1526 -8.4; 1678 -11.6; 1846 -15.0; 2031 -17.7; 2234 -20.0; 2457 -17.2; 2703 -16.3; 2973 -14.4; 3270 -7.9; 3597 -6.5; 3957 -8.7; 4353 -8.5; 4788 -10.0; 5267 -13.8; 5793 -20.2; 6373 -22.2; 7010 -19.7; 7711 -18.9; 8482 -21.4; 9330 -23.8; 10263 -22.8; 11289 -19.5; 12418 -17.9; 13660 -20.0; 15026 -21.0; 16529 -17.3; 18182 -14.0; 20000 -12.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Howard Leight Sync GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Howard Leight Sync ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.1dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 208 Hz   |  0.87 | -12.1 dB |
| Peaking | 2239 Hz  |  3    | -13.7 dB |
| Peaking | 6210 Hz  |  4.19 | -11.8 dB |
| Peaking | 9436 Hz  |  1.99 | -12.2 dB |
| Peaking | 15271 Hz |  0.66 | -12.8 dB |
| Peaking | 28 Hz    |  0.49 | 6.3 dB   |
| Peaking | 56 Hz    |  2.21 | 3.9 dB   |
| Peaking | 125 Hz   |  2.53 | -4.9 dB  |
| Peaking | 1256 Hz  |  4.56 | 2.7 dB   |
| Peaking | 3472 Hz  | 11.28 | 5.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB   |
| Peaking | 62 Hz    | 1.41 | 6.2 dB   |
| Peaking | 125 Hz   | 1.41 | -10.2 dB |
| Peaking | 250 Hz   | 1.41 | -8.6 dB  |
| Peaking | 500 Hz   | 1.41 | -4.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.1 dB   |
| Peaking | 2000 Hz  | 1.41 | -10.9 dB |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB   |
| Peaking | 8000 Hz  | 1.41 | -18.5 dB |
| Peaking | 16000 Hz | 1.41 | -16.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Howard%20Leight%20Sync/Howard%20Leight%20Sync.png)