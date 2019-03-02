# Anker SoundCore Space NC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -18.7; 23 -18.5; 25 -18.3; 28 -17.9; 31 -17.5; 34 -17.1; 37 -16.7; 41 -16.3; 45 -16.0; 49 -15.8; 54 -15.7; 60 -15.6; 66 -15.6; 72 -15.4; 79 -15.3; 87 -15.2; 96 -14.9; 106 -14.5; 116 -14.1; 128 -13.5; 141 -12.7; 155 -11.8; 170 -10.8; 187 -9.6; 206 -8.1; 227 -6.9; 249 -6.2; 274 -5.3; 302 -4.5; 332 -4.0; 365 -3.8; 402 -3.8; 442 -4.0; 486 -4.2; 535 -4.1; 588 -4.0; 647 -3.9; 712 -3.9; 783 -3.8; 861 -3.7; 947 -4.1; 1042 -4.4; 1146 -5.6; 1261 -6.7; 1387 -7.3; 1526 -7.6; 1678 -8.2; 1846 -9.3; 2031 -9.6; 2234 -9.8; 2457 -9.7; 2703 -9.8; 2973 -10.0; 3270 -9.4; 3597 -9.3; 3957 -6.8; 4353 -2.9; 4788 -0.5; 5267 -0.5; 5793 -2.1; 6373 -5.8; 7010 -4.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -7.6; 13660 -8.3; 15026 -8.6; 16529 -7.9; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Anker SoundCore Space NC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Anker SoundCore Space NC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 14 Hz    |  0.21 | -12.3 dB |
| Peaking | 121 Hz   |  0.73 | -7.2 dB  |
| Peaking | 400 Hz   |  0.27 | 4.8 dB   |
| Peaking | 3393 Hz  |  0.55 | -8.0 dB  |
| Peaking | 5014 Hz  |  1.66 | 12.6 dB  |
| Peaking | 340 Hz   |  1.56 | 1.6 dB   |
| Peaking | 445 Hz   |  0.88 | -1.3 dB  |
| Peaking | 898 Hz   |  2.91 | 1.2 dB   |
| Peaking | 6277 Hz  | 14.44 | -1.7 dB  |
| Peaking | 15157 Hz |  2.36 | -2.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -11.8 dB |
| Peaking | 62 Hz    | 1.41 | -6.2 dB  |
| Peaking | 125 Hz   | 1.41 | -6.8 dB  |
| Peaking | 250 Hz   | 1.41 | 1.8 dB   |
| Peaking | 500 Hz   | 1.41 | 2.7 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.7 dB   |
| Peaking | 2000 Hz  | 1.41 | -5.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 16000 Hz | 1.41 | -2.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Anker%20SoundCore%20Space%20NC/Anker%20SoundCore%20Space%20NC.png)