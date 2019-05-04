# Bose SoundLink On-Ear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.7; 23 -7.8; 25 -7.9; 28 -7.9; 31 -7.9; 34 -7.9; 37 -7.8; 41 -7.7; 45 -7.6; 49 -7.5; 54 -7.3; 60 -7.3; 66 -7.3; 72 -7.2; 79 -7.3; 87 -7.3; 96 -7.3; 106 -7.3; 116 -7.3; 128 -7.3; 141 -7.4; 155 -7.4; 170 -7.1; 187 -6.6; 206 -6.2; 227 -6.0; 249 -6.0; 274 -6.0; 302 -6.0; 332 -5.8; 365 -5.3; 402 -4.8; 442 -4.4; 486 -4.0; 535 -3.4; 588 -2.9; 647 -2.4; 712 -2.0; 783 -1.7; 861 -1.5; 947 -1.1; 1042 -1.0; 1146 -1.0; 1261 -1.0; 1387 -1.0; 1526 -1.2; 1678 -1.6; 1846 -2.2; 2031 -3.1; 2234 -3.4; 2457 -2.9; 2703 -3.5; 2973 -3.9; 3270 -3.7; 3597 -4.4; 3957 -5.0; 4353 -4.6; 4788 -3.8; 5267 -1.9; 5793 -0.5; 6373 -0.9; 7010 -4.3; 7711 -6.8; 8482 -6.8; 9330 -5.6; 10263 -5.8; 11289 -5.7; 12418 -4.3; 13660 -4.0; 15026 -6.1; 16529 -11.2; 18182 -14.2; 20000 -11.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose SoundLink On-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose SoundLink On-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 24 Hz    | 0.58 | -3.4 dB  |
| Peaking | 139 Hz   | 0.42 | -2.9 dB  |
| Peaking | 1060 Hz  | 0.89 | 3.6 dB   |
| Peaking | 5922 Hz  | 6.57 | 4.5 dB   |
| Peaking | 18661 Hz | 0.86 | -11.0 dB |
| Peaking | 1575 Hz  | 6.13 | 0.6 dB   |
| Peaking | 4011 Hz  | 4.61 | -1.4 dB  |
| Peaking | 6753 Hz  | 2.59 | 3.1 dB   |
| Peaking | 7658 Hz  | 2.25 | -4.3 dB  |
| Peaking | 13725 Hz | 3.34 | 2.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.0 dB |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.0 dB |
| Peaking | 1000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -6.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bose%20SoundLink%20On-Ear/Bose%20SoundLink%20On-Ear.png)