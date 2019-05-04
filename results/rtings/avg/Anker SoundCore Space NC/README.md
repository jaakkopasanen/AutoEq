# Anker SoundCore Space NC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -18.5; 23 -18.3; 25 -18.1; 28 -17.7; 31 -17.3; 34 -16.9; 37 -16.5; 41 -16.1; 45 -15.8; 49 -15.6; 54 -15.5; 60 -15.4; 66 -15.4; 72 -15.3; 79 -15.1; 87 -15.0; 96 -14.7; 106 -14.3; 116 -13.8; 128 -13.3; 141 -12.5; 155 -11.6; 170 -10.6; 187 -9.4; 206 -8.0; 227 -6.8; 249 -6.1; 274 -5.3; 302 -4.5; 332 -3.9; 365 -3.7; 402 -3.8; 442 -4.0; 486 -4.2; 535 -4.2; 588 -4.1; 647 -4.0; 712 -4.0; 783 -3.9; 861 -3.8; 947 -4.2; 1042 -4.6; 1146 -5.7; 1261 -6.9; 1387 -7.5; 1526 -7.8; 1678 -8.5; 1846 -9.5; 2031 -10.1; 2234 -10.5; 2457 -10.6; 2703 -10.5; 2973 -10.1; 3270 -9.2; 3597 -9.1; 3957 -6.5; 4353 -2.6; 4788 -0.6; 5267 -0.5; 5793 -2.0; 6373 -4.6; 7010 -4.2; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.7; 12418 -7.7; 13660 -7.5; 15026 -8.1; 16529 -7.8; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Anker SoundCore Space NC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Anker SoundCore Space NC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 14 Hz    | 0.22 | -12.1 dB |
| Peaking | 120 Hz   | 0.72 | -7.0 dB  |
| Peaking | 497 Hz   | 0.23 | 5.1 dB   |
| Peaking | 3396 Hz  | 0.5  | -11.1 dB |
| Peaking | 4956 Hz  | 1.3  | 14.8 dB  |
| Peaking | 327 Hz   | 1.51 | 1.6 dB   |
| Peaking | 520 Hz   | 0.47 | -1.5 dB  |
| Peaking | 903 Hz   | 2.05 | 1.8 dB   |
| Peaking | 10250 Hz | 3.97 | 0.8 dB   |
| Peaking | 15462 Hz | 2.16 | -1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -11.6 dB |
| Peaking | 62 Hz    | 1.41 | -6.1 dB  |
| Peaking | 125 Hz   | 1.41 | -6.7 dB  |
| Peaking | 250 Hz   | 1.41 | 1.8 dB   |
| Peaking | 500 Hz   | 1.41 | 2.7 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.8 dB   |
| Peaking | 2000 Hz  | 1.41 | -5.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 16000 Hz | 1.41 | -2.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Anker%20SoundCore%20Space%20NC/Anker%20SoundCore%20Space%20NC.png)