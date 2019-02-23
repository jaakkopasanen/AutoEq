# RHA T10i Treble Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.1; 23 -13.2; 25 -13.3; 28 -13.6; 31 -13.9; 34 -14.1; 37 -14.1; 41 -14.2; 45 -14.3; 49 -14.4; 54 -14.5; 60 -14.6; 66 -14.6; 72 -14.7; 79 -14.8; 87 -14.8; 96 -14.9; 106 -14.8; 116 -14.5; 128 -14.4; 141 -14.2; 155 -13.9; 170 -13.5; 187 -13.1; 206 -12.6; 227 -12.0; 249 -11.5; 274 -10.8; 302 -10.2; 332 -9.5; 365 -8.8; 402 -8.2; 442 -7.4; 486 -6.9; 535 -6.2; 588 -5.3; 647 -4.7; 712 -4.6; 783 -4.0; 861 -3.6; 947 -3.2; 1042 -3.6; 1146 -3.9; 1261 -4.3; 1387 -5.1; 1526 -5.9; 1678 -6.9; 1846 -7.6; 2031 -8.6; 2234 -9.9; 2457 -10.4; 2703 -9.5; 2973 -7.4; 3270 -5.6; 3597 -5.2; 3957 -3.6; 4353 -1.3; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.5; 8482 -14.6; 9330 -16.9; 10263 -13.3; 11289 -6.6; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`RHA T10i Treble Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RHA T10i Treble Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 42 Hz    | 0.25 | -7.2 dB  |
| Peaking | 177 Hz   | 0.56 | -3.8 dB  |
| Peaking | 2427 Hz  | 1.02 | -16.0 dB |
| Peaking | 3366 Hz  | 0.29 | 12.7 dB  |
| Peaking | 9280 Hz  | 2.54 | -17.9 dB |
| Peaking | 878 Hz   | 3.49 | 0.9 dB   |
| Peaking | 3725 Hz  | 4.46 | -2.4 dB  |
| Peaking | 6534 Hz  | 0.84 | 1.5 dB   |
| Peaking | 8404 Hz  | 8    | -3.6 dB  |
| Peaking | 15277 Hz | 1.26 | -1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.2 dB |
| Peaking | 62 Hz    | 1.41 | -6.1 dB |
| Peaking | 125 Hz   | 1.41 | -6.8 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.2 dB |
| Peaking | 4000 Hz  | 1.41 | 6.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/RHA%20T10i%20Treble%20Filter/RHA%20T10i%20Treble%20Filter.png)