# Anker SoundBuds Life
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.0; 23 -8.3; 25 -8.6; 28 -8.8; 31 -8.9; 34 -8.8; 37 -8.6; 41 -8.3; 45 -7.9; 49 -7.6; 54 -7.3; 60 -7.3; 66 -7.3; 72 -7.4; 79 -7.4; 87 -7.6; 96 -7.8; 106 -8.1; 116 -8.4; 128 -8.7; 141 -8.9; 155 -9.1; 170 -9.3; 187 -9.5; 206 -8.6; 227 -7.2; 249 -5.8; 274 -4.3; 302 -3.6; 332 -3.7; 365 -4.0; 402 -4.1; 442 -3.8; 486 -3.4; 535 -2.7; 588 -2.0; 647 -1.4; 712 -1.0; 783 -0.6; 861 -0.5; 947 -0.9; 1042 -1.8; 1146 -2.7; 1261 -3.4; 1387 -3.8; 1526 -4.3; 1678 -5.1; 1846 -5.8; 2031 -6.3; 2234 -6.1; 2457 -6.1; 2703 -7.1; 2973 -8.8; 3270 -9.8; 3597 -9.7; 3957 -9.8; 4353 -10.9; 4788 -12.4; 5267 -14.2; 5793 -11.9; 6373 -8.0; 7010 -5.7; 7711 -6.0; 8482 -4.9; 9330 -1.5; 10263 -1.4; 11289 -1.4; 12418 -1.4; 13660 -1.5; 15026 -5.5; 16529 -5.9; 18182 -6.5; 20000 -12.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Anker SoundBuds Life GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Anker SoundBuds Life ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 0.5  | -7.0 dB |
| Peaking | 137 Hz   | 0.79 | -5.6 dB |
| Peaking | 194 Hz   | 2.64 | -3.1 dB |
| Peaking | 3403 Hz  | 0.82 | -6.9 dB |
| Peaking | 5346 Hz  | 2.7  | -8.8 dB |
| Peaking | 437 Hz   | 3.52 | -1.5 dB |
| Peaking | 825 Hz   | 2.21 | 2.1 dB  |
| Peaking | 1674 Hz  | 2.79 | -1.2 dB |
| Peaking | 11632 Hz | 1.64 | 2.6 dB  |
| Peaking | 20314 Hz | 0.34 | -9.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -8.0 dB  |
| Peaking | 62 Hz    | 1.41 | -3.1 dB  |
| Peaking | 125 Hz   | 1.41 | -6.9 dB  |
| Peaking | 250 Hz   | 1.41 | -3.7 dB  |
| Peaking | 500 Hz   | 1.41 | -0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 2000 Hz  | 1.41 | -2.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -10.8 dB |
| Peaking | 8000 Hz  | 1.41 | -2.0 dB  |
| Peaking | 16000 Hz | 1.41 | -4.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Anker%20SoundBuds%20Life/Anker%20SoundBuds%20Life.png)