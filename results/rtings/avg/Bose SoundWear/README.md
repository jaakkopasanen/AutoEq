# Bose SoundWear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -1.3; 155 -2.7; 170 -3.9; 187 -3.9; 206 -3.0; 227 -0.5; 249 -1.9; 274 -3.0; 302 -4.5; 332 -5.7; 365 -4.6; 402 -8.1; 442 -8.0; 486 -8.4; 535 -10.1; 588 -8.6; 647 -5.9; 712 -7.3; 783 -8.6; 861 -8.4; 947 -6.6; 1042 -4.8; 1146 -5.6; 1261 -7.8; 1387 -2.9; 1526 -1.7; 1678 -2.1; 1846 -5.3; 2031 -8.9; 2234 -9.8; 2457 -8.4; 2703 -9.0; 2973 -10.2; 3270 -13.0; 3597 -13.9; 3957 -12.3; 4353 -14.2; 4788 -13.4; 5267 -12.9; 5793 -7.3; 6373 -6.9; 7010 -4.4; 7711 -6.2; 8482 -8.8; 9330 -9.8; 10263 -7.1; 11289 -8.9; 12418 -14.6; 13660 -17.5; 15026 -17.3; 16529 -11.9; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose SoundWear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose SoundWear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 0.3  | 5.8 dB   |
| Peaking | 122 Hz   | 0.76 | 3.6 dB   |
| Peaking | 1566 Hz  | 6.06 | 6.9 dB   |
| Peaking | 3896 Hz  | 1.64 | -7.8 dB  |
| Peaking | 14355 Hz | 1.87 | -12.6 dB |
| Peaking | 182 Hz   | 3.7  | -2.6 dB  |
| Peaking | 233 Hz   | 3.23 | 4.1 dB   |
| Peaking | 512 Hz   | 2.48 | -3.6 dB  |
| Peaking | 5182 Hz  | 5.09 | -4.3 dB  |
| Peaking | 6453 Hz  | 2.58 | 4.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB   |
| Peaking | 62 Hz    | 1.41 | 4.7 dB   |
| Peaking | 125 Hz   | 1.41 | 4.1 dB   |
| Peaking | 250 Hz   | 1.41 | 3.7 dB   |
| Peaking | 500 Hz   | 1.41 | -3.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.9 dB   |
| Peaking | 4000 Hz  | 1.41 | -8.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 16000 Hz | 1.41 | -11.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bose%20SoundWear/Bose%20SoundWear.png)