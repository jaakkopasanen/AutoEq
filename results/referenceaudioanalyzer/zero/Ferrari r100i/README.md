# Ferrari r100i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -18.3; 23 -18.5; 25 -18.7; 28 -18.9; 31 -19.0; 34 -19.1; 37 -19.1; 41 -19.0; 45 -18.9; 49 -18.8; 54 -18.6; 60 -18.4; 66 -18.2; 72 -18.0; 79 -17.8; 87 -17.4; 96 -17.0; 106 -16.5; 116 -16.0; 128 -15.5; 141 -15.0; 155 -14.5; 170 -13.8; 187 -13.0; 206 -12.5; 227 -12.6; 249 -12.5; 274 -11.9; 302 -11.1; 332 -10.2; 365 -9.4; 402 -8.6; 442 -7.8; 486 -7.1; 535 -6.4; 588 -5.6; 647 -4.7; 712 -3.7; 783 -2.8; 861 -1.9; 947 -0.8; 1042 -0.5; 1146 -0.5; 1261 -0.5; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -2.0; 2973 -3.9; 3270 -5.7; 3597 -7.6; 3957 -9.2; 4353 -10.0; 4788 -10.6; 5267 -11.3; 5793 -11.4; 6373 -9.5; 7010 -5.4; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ferrari r100i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ferrari r100i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 0.13 | -12.4 dB |
| Peaking | 1104 Hz  | 0.84 | 6.5 dB   |
| Peaking | 2349 Hz  | 1.61 | 5.3 dB   |
| Peaking | 5325 Hz  | 1.19 | -7.1 dB  |
| Peaking | 7294 Hz  | 2.41 | 4.4 dB   |
| Peaking | 205 Hz   | 2.08 | 1.2 dB   |
| Peaking | 252 Hz   | 2.54 | -1.5 dB  |
| Peaking | 7979 Hz  | 8    | -0.8 dB  |
| Peaking | 10791 Hz | 1.39 | 0.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -12.9 dB |
| Peaking | 62 Hz    | 1.41 | -8.9 dB  |
| Peaking | 125 Hz   | 1.41 | -6.8 dB  |
| Peaking | 250 Hz   | 1.41 | -4.6 dB  |
| Peaking | 500 Hz   | 1.41 | -0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 5.2 dB   |
| Peaking | 2000 Hz  | 1.41 | 7.4 dB   |
| Peaking | 4000 Hz  | 1.41 | -4.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB  |
| Peaking | 16000 Hz | 1.41 | 0.1 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Ferrari%20r100i/Ferrari%20r100i.png)