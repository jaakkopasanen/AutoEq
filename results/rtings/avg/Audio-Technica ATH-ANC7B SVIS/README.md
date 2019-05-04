# Audio-Technica ATH-ANC7B SVIS
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.9; 23 -4.6; 25 -5.2; 28 -6.0; 31 -6.6; 34 -7.2; 37 -7.6; 41 -8.1; 45 -8.4; 49 -8.8; 54 -9.3; 60 -9.8; 66 -10.0; 72 -10.2; 79 -10.3; 87 -10.5; 96 -10.9; 106 -11.6; 116 -12.1; 128 -12.3; 141 -12.3; 155 -12.3; 170 -12.1; 187 -11.8; 206 -11.5; 227 -11.3; 249 -11.1; 274 -10.9; 302 -10.8; 332 -10.6; 365 -10.5; 402 -10.5; 442 -10.7; 486 -11.1; 535 -11.5; 588 -12.1; 647 -11.3; 712 -8.7; 783 -7.6; 861 -8.7; 947 -10.2; 1042 -8.2; 1146 -4.4; 1261 -3.2; 1387 -2.1; 1526 -0.6; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -1.3; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -1.3; 4353 -1.2; 4788 -2.6; 5267 -6.4; 5793 -7.3; 6373 -3.6; 7010 -4.0; 7711 -8.3; 8482 -9.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -11.7; 13660 -15.7; 15026 -16.5; 16529 -18.3; 18182 -18.3; 20000 -7.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-ANC7B SVIS GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-ANC7B SVIS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 60 Hz    | 2.05 | -1.7 dB  |
| Peaking | 138 Hz   | 0.8  | -5.1 dB  |
| Peaking | 750 Hz   | 0.55 | -8.9 dB  |
| Peaking | 1760 Hz  | 0.46 | 10.3 dB  |
| Peaking | 16971 Hz | 0.76 | -13.4 dB |
| Peaking | 19 Hz    | 2.46 | 3.1 dB   |
| Peaking | 930 Hz   | 2.35 | 3.7 dB   |
| Peaking | 965 Hz   | 5.33 | -6.8 dB  |
| Peaking | 8112 Hz  | 9.86 | -4.0 dB  |
| Peaking | 10801 Hz | 4.46 | 3.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB   |
| Peaking | 62 Hz    | 1.41 | -2.6 dB  |
| Peaking | 125 Hz   | 1.41 | -5.1 dB  |
| Peaking | 250 Hz   | 1.41 | -3.1 dB  |
| Peaking | 500 Hz   | 1.41 | -4.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 7.1 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.4 dB   |
| Peaking | 8000 Hz  | 1.41 | -0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -15.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-ANC7B%20SVIS/Audio-Technica%20ATH-ANC7B%20SVIS.png)