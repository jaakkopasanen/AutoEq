# Anker SoundBuds Life
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.7; 23 -13.0; 25 -13.3; 28 -13.5; 31 -13.6; 34 -13.5; 37 -13.4; 41 -13.0; 45 -12.7; 49 -12.3; 54 -11.9; 60 -11.6; 66 -11.4; 72 -11.2; 79 -11.1; 87 -10.9; 96 -10.8; 106 -10.7; 116 -10.5; 128 -10.3; 141 -10.1; 155 -9.9; 170 -9.8; 187 -9.6; 206 -8.6; 227 -7.0; 249 -5.5; 274 -4.0; 302 -3.3; 332 -3.5; 365 -3.8; 402 -3.8; 442 -3.6; 486 -3.2; 535 -2.6; 588 -1.9; 647 -1.3; 712 -1.0; 783 -0.6; 861 -0.5; 947 -0.9; 1042 -1.8; 1146 -2.7; 1261 -3.4; 1387 -3.9; 1526 -4.5; 1678 -5.3; 1846 -6.1; 2031 -6.6; 2234 -6.8; 2457 -6.8; 2703 -7.6; 2973 -8.8; 3270 -9.4; 3597 -9.2; 3957 -9.3; 4353 -10.3; 4788 -12.6; 5267 -14.4; 5793 -11.6; 6373 -6.8; 7010 -5.6; 7711 -6.6; 8482 -5.9; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.4; 20000 -12.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Anker SoundBuds Life GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Anker SoundBuds Life ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.08 | -6.7 dB |
| Peaking | 301 Hz  | 2.41 | 4.0 dB  |
| Peaking | 775 Hz  | 0.97 | 6.0 dB  |
| Peaking | 3297 Hz | 1.45 | -3.2 dB |
| Peaking | 5191 Hz | 4.4  | -8.2 dB |
| Peaking | 35 Hz   | 1.28 | -2.0 dB |
| Peaking | 53 Hz   | 0.66 | 1.2 dB  |
| Peaking | 186 Hz  | 4.65 | -1.2 dB |
| Peaking | 6799 Hz | 9.01 | 2.0 dB  |
| Peaking | 9025 Hz | 4.24 | 0.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.3 dB |
| Peaking | 62 Hz    | 1.41 | -3.5 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | 0.4 dB  |
| Peaking | 500 Hz   | 1.41 | 3.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB |
| Peaking | 4000 Hz  | 1.41 | -5.8 dB |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Anker%20SoundBuds%20Life/Anker%20SoundBuds%20Life.png)