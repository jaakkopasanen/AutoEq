# Dunu Hephaes (DN-16)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -18.7; 23 -18.7; 25 -18.7; 28 -18.7; 31 -18.7; 34 -18.7; 37 -18.7; 41 -18.7; 45 -18.6; 49 -18.5; 54 -18.4; 60 -18.2; 66 -18.0; 72 -17.8; 79 -17.6; 87 -17.4; 96 -17.1; 106 -16.8; 116 -16.4; 128 -16.1; 141 -15.6; 155 -15.2; 170 -15.0; 187 -14.7; 206 -14.3; 227 -13.7; 249 -13.1; 274 -12.4; 302 -11.6; 332 -10.9; 365 -10.1; 402 -9.2; 442 -8.3; 486 -7.3; 535 -6.4; 588 -5.4; 647 -4.5; 712 -3.4; 783 -2.4; 861 -1.7; 947 -1.1; 1042 -0.7; 1146 -0.5; 1261 -0.5; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -2.0; 2973 -5.0; 3270 -7.6; 3597 -9.0; 3957 -9.7; 4353 -10.0; 4788 -10.3; 5267 -10.6; 5793 -10.2; 6373 -7.7; 7010 -4.4; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Dunu Hephaes (DN-16) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dunu Hephaes (DN-16) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 28 Hz    | 0.08 | -11.9 dB |
| Peaking | 1877 Hz  | 0.32 | 9.1 dB   |
| Peaking | 4293 Hz  | 1.1  | -10.7 dB |
| Peaking | 20554 Hz | 2.85 | -0.4 dB  |
| Peaking | 2529 Hz  | 3.4  | 3.5 dB   |
| Peaking | 3663 Hz  | 0.95 | -3.4 dB  |
| Peaking | 4367 Hz  | 2.5  | 4.2 dB   |
| Peaking | 5873 Hz  | 3.07 | -1.7 dB  |
| Peaking | 6863 Hz  | 5.72 | 4.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -12.9 dB |
| Peaking | 62 Hz    | 1.41 | -8.4 dB  |
| Peaking | 125 Hz   | 1.41 | -7.5 dB  |
| Peaking | 250 Hz   | 1.41 | -5.6 dB  |
| Peaking | 500 Hz   | 1.41 | -0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 5.3 dB   |
| Peaking | 2000 Hz  | 1.41 | 7.3 dB   |
| Peaking | 4000 Hz  | 1.41 | -5.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 16000 Hz | 1.41 | -0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Dunu%20Hephaes%20(DN-16)/Dunu%20Hephaes%20(DN-16).png)