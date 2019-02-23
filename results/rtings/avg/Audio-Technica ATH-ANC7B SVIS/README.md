# Audio-Technica ATH-ANC7B SVIS
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.1; 23 -4.8; 25 -5.4; 28 -6.2; 31 -6.8; 34 -7.3; 37 -7.8; 41 -8.2; 45 -8.6; 49 -9.0; 54 -9.5; 60 -10.0; 66 -10.2; 72 -10.4; 79 -10.6; 87 -10.7; 96 -11.1; 106 -11.7; 116 -12.2; 128 -12.4; 141 -12.5; 155 -12.6; 170 -12.4; 187 -12.0; 206 -11.7; 227 -11.4; 249 -11.2; 274 -11.0; 302 -10.8; 332 -10.6; 365 -10.5; 402 -10.6; 442 -10.7; 486 -11.1; 535 -11.5; 588 -12.1; 647 -11.1; 712 -8.5; 783 -7.5; 861 -8.6; 947 -10.2; 1042 -7.8; 1146 -4.2; 1261 -3.2; 1387 -1.7; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -1.7; 4353 -1.6; 4788 -2.2; 5267 -6.0; 5793 -7.5; 6373 -4.5; 7010 -4.0; 7711 -7.7; 8482 -9.8; 9330 -6.6; 10263 -6.5; 11289 -6.5; 12418 -11.8; 13660 -16.6; 15026 -16.9; 16529 -18.5; 18182 -18.3; 20000 -6.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-ANC7B SVIS GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-ANC7B SVIS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 61 Hz    | 1.82 | -1.8 dB  |
| Peaking | 139 Hz   | 0.8  | -5.3 dB  |
| Peaking | 759 Hz   | 0.53 | -9.1 dB  |
| Peaking | 1731 Hz  | 0.46 | 10.7 dB  |
| Peaking | 16869 Hz | 0.77 | -13.6 dB |
| Peaking | 20 Hz    | 2.4  | 2.7 dB   |
| Peaking | 914 Hz   | 2.33 | 3.9 dB   |
| Peaking | 974 Hz   | 5.31 | -7.1 dB  |
| Peaking | 8277 Hz  | 9.41 | -3.8 dB  |
| Peaking | 10899 Hz | 4.55 | 3.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.7 dB   |
| Peaking | 62 Hz    | 1.41 | -2.8 dB  |
| Peaking | 125 Hz   | 1.41 | -5.3 dB  |
| Peaking | 250 Hz   | 1.41 | -3.2 dB  |
| Peaking | 500 Hz   | 1.41 | -4.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 7.2 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.3 dB   |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -15.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-ANC7B%20SVIS/Audio-Technica%20ATH-ANC7B%20SVIS.png)