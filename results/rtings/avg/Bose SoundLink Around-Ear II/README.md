# Bose SoundLink Around-Ear II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.4; 23 -7.4; 25 -7.4; 28 -7.4; 31 -7.3; 34 -7.1; 37 -6.9; 41 -6.6; 45 -6.3; 49 -6.1; 54 -5.9; 60 -5.7; 66 -5.7; 72 -5.7; 79 -5.8; 87 -5.9; 96 -6.0; 106 -6.2; 116 -6.3; 128 -6.5; 141 -6.4; 155 -6.4; 170 -6.4; 187 -6.2; 206 -6.1; 227 -6.1; 249 -5.9; 274 -5.8; 302 -5.8; 332 -5.7; 365 -5.5; 402 -5.6; 442 -5.7; 486 -5.5; 535 -5.4; 588 -5.2; 647 -5.1; 712 -4.9; 783 -4.5; 861 -3.7; 947 -3.3; 1042 -3.4; 1146 -4.2; 1261 -4.9; 1387 -5.7; 1526 -5.9; 1678 -5.8; 1846 -8.3; 2031 -9.1; 2234 -7.8; 2457 -6.6; 2703 -6.6; 2973 -7.7; 3270 -8.5; 3597 -8.3; 3957 -7.7; 4353 -7.1; 4788 -4.6; 5267 -0.5; 5793 -3.9; 6373 -4.7; 7010 -3.0; 7711 -3.0; 8482 -3.3; 9330 -3.6; 10263 -3.3; 11289 -3.3; 12418 -3.9; 13660 -8.5; 15026 -9.7; 16529 -9.5; 18182 -8.4; 20000 -5.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose SoundLink Around-Ear II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose SoundLink Around-Ear II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 0.83 | -3.9 dB |
| Peaking | 187 Hz   | 0.34 | -2.9 dB |
| Peaking | 2002 Hz  | 2.76 | -5.1 dB |
| Peaking | 3464 Hz  | 2.72 | -5.2 dB |
| Peaking | 16615 Hz | 1.06 | -7.3 dB |
| Peaking | 966 Hz   | 6.66 | 1.3 dB  |
| Peaking | 4412 Hz  | 5.7  | -2.1 dB |
| Peaking | 5265 Hz  | 9.25 | 4.5 dB  |
| Peaking | 12510 Hz | 1.4  | 3.1 dB  |
| Peaking | 13869 Hz | 2.85 | -4.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.4 dB |
| Peaking | 62 Hz    | 1.41 | -1.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.6 dB |
| Peaking | 4000 Hz  | 1.41 | -3.2 dB |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 16000 Hz | 1.41 | -8.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bose%20SoundLink%20Around-Ear%20II/Bose%20SoundLink%20Around-Ear%20II.png)