# Monster iSport Victory In-Ear Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -20.6; 23 -21.6; 25 -22.3; 28 -22.7; 31 -22.6; 34 -22.3; 37 -22.0; 41 -21.9; 45 -21.6; 49 -21.3; 54 -20.7; 60 -20.0; 66 -19.3; 72 -18.3; 79 -17.1; 87 -15.6; 96 -13.7; 106 -11.8; 116 -10.2; 128 -9.6; 141 -9.9; 155 -10.3; 170 -10.3; 187 -9.8; 206 -8.8; 227 -7.7; 249 -7.5; 274 -8.2; 302 -9.0; 332 -9.4; 365 -9.3; 402 -9.3; 442 -9.0; 486 -8.6; 535 -8.1; 588 -7.6; 647 -7.2; 712 -6.7; 783 -6.3; 861 -5.9; 947 -5.4; 1042 -4.9; 1146 -4.8; 1261 -4.7; 1387 -4.3; 1526 -4.1; 1678 -4.5; 1846 -5.2; 2031 -6.1; 2234 -7.1; 2457 -8.1; 2703 -8.8; 2973 -8.7; 3270 -7.5; 3597 -5.5; 3957 -3.6; 4353 -2.1; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -4.1; 7010 -9.0; 7711 -9.0; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster iSport Victory In-Ear Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster iSport Victory In-Ear Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 28 Hz   | 0.56 | -15.3 dB |
| Peaking | 62 Hz   | 1.24 | -6.0 dB  |
| Peaking | 386 Hz  | 2.22 | -2.7 dB  |
| Peaking | 2861 Hz | 4.64 | -3.5 dB  |
| Peaking | 4993 Hz | 2.76 | 7.0 dB   |
| Peaking | 121 Hz  | 5.62 | 1.6 dB   |
| Peaking | 173 Hz  | 4.85 | -1.5 dB  |
| Peaking | 1360 Hz | 1.9  | 2.5 dB   |
| Peaking | 6000 Hz | 7.65 | 4.0 dB   |
| Peaking | 7184 Hz | 4.32 | -4.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -17.4 dB |
| Peaking | 62 Hz    | 1.41 | -10.2 dB |
| Peaking | 125 Hz   | 1.41 | -0.9 dB  |
| Peaking | 250 Hz   | 1.41 | -0.9 dB  |
| Peaking | 500 Hz   | 1.41 | -2.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.8 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.6 dB   |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Monster%20iSport%20Victory%20In-Ear%20Wireless/Monster%20iSport%20Victory%20In-Ear%20Wireless.png)