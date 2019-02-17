# Audio-Technica ATH-ANC7B SVIS
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.9; 23 -1.6; 25 -2.2; 28 -3.0; 31 -3.6; 34 -4.2; 37 -4.6; 41 -5.0; 45 -5.4; 49 -5.8; 54 -6.3; 60 -6.8; 66 -7.0; 72 -7.2; 79 -7.4; 87 -7.5; 96 -7.9; 106 -8.5; 116 -9.1; 128 -9.3; 141 -9.4; 155 -9.4; 170 -9.2; 187 -8.8; 206 -8.5; 227 -8.2; 249 -8.0; 274 -7.8; 302 -7.6; 332 -7.4; 365 -7.3; 402 -7.4; 442 -7.5; 486 -7.9; 535 -8.3; 588 -8.9; 647 -7.9; 712 -5.3; 783 -4.3; 861 -5.5; 947 -7.0; 1042 -4.7; 1146 -1.1; 1261 -0.5; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -2.8; 5793 -4.3; 6373 -1.6; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -8.7; 13660 -13.4; 15026 -13.7; 16529 -15.3; 18182 -15.2; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-ANC7B SVIS GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-ANC7B SVIS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 17 Hz    | 0.55 | 6.7 dB   |
| Peaking | 172 Hz   | 0.16 | -2.4 dB  |
| Peaking | 1347 Hz  | 2.25 | 4.0 dB   |
| Peaking | 3124 Hz  | 0.51 | 6.5 dB   |
| Peaking | 16766 Hz | 0.81 | -10.0 dB |
| Peaking | 611 Hz   | 3.02 | -5.7 dB  |
| Peaking | 670 Hz   | 1.36 | 4.4 dB   |
| Peaking | 950 Hz   | 6.07 | -4.2 dB  |
| Peaking | 7974 Hz  | 6.95 | -1.6 dB  |
| Peaking | 11526 Hz | 6.88 | 2.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 3.9 dB   |
| Peaking | 62 Hz    | 1.41 | -0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -2.8 dB  |
| Peaking | 250 Hz   | 1.41 | -0.8 dB  |
| Peaking | 500 Hz   | 1.41 | -2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 2000 Hz  | 1.41 | 5.9 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB   |
| Peaking | 16000 Hz | 1.41 | -11.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-ANC7B%20SVIS/Audio-Technica%20ATH-ANC7B%20SVIS.png)