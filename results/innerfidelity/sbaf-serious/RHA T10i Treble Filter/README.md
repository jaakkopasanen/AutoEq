# RHA T10i Treble Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -16.2; 23 -16.2; 25 -16.3; 28 -16.7; 31 -17.0; 34 -17.1; 37 -17.2; 41 -17.3; 45 -17.4; 49 -17.4; 54 -17.5; 60 -17.6; 66 -17.7; 72 -17.7; 79 -17.8; 87 -17.9; 96 -18.0; 106 -17.8; 116 -17.6; 128 -17.5; 141 -17.3; 155 -17.0; 170 -16.6; 187 -16.2; 206 -15.7; 227 -15.1; 249 -14.6; 274 -13.9; 302 -13.2; 332 -12.6; 365 -11.9; 402 -11.2; 442 -10.4; 486 -9.9; 535 -9.3; 588 -8.4; 647 -7.8; 712 -7.7; 783 -7.0; 861 -6.6; 947 -6.3; 1042 -6.6; 1146 -6.9; 1261 -7.3; 1387 -8.1; 1526 -9.0; 1678 -9.9; 1846 -10.7; 2031 -11.6; 2234 -12.9; 2457 -13.5; 2703 -12.6; 2973 -10.4; 3270 -8.6; 3597 -8.2; 3957 -6.6; 4353 -4.3; 4788 -0.7; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -8.1; 8482 -17.6; 9330 -19.9; 10263 -16.4; 11289 -7.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`RHA T10i Treble Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RHA T10i Treble Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 42 Hz    | 0.24 | -10.4 dB |
| Peaking | 187 Hz   | 0.64 | -4.8 dB  |
| Peaking | 2473 Hz  | 1.68 | -7.8 dB  |
| Peaking | 5899 Hz  | 1.46 | 9.5 dB   |
| Peaking | 9124 Hz  | 3.04 | -17.7 dB |
| Peaking | 920 Hz   | 1.19 | 3.5 dB   |
| Peaking | 945 Hz   | 0.6  | -2.0 dB  |
| Peaking | 10320 Hz | 5.75 | -4.8 dB  |
| Peaking | 11527 Hz | 3    | 3.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.3 dB |
| Peaking | 62 Hz    | 1.41 | -8.2 dB  |
| Peaking | 125 Hz   | 1.41 | -9.0 dB  |
| Peaking | 250 Hz   | 1.41 | -6.4 dB  |
| Peaking | 500 Hz   | 1.41 | -2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.7 dB   |
| Peaking | 2000 Hz  | 1.41 | -7.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB   |
| Peaking | 8000 Hz  | 1.41 | -5.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/RHA%20T10i%20Treble%20Filter/RHA%20T10i%20Treble%20Filter.png)