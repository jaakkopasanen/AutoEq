# Bose SoundLink Around-Ear II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.7; 23 -6.8; 25 -6.8; 28 -6.8; 31 -6.7; 34 -6.5; 37 -6.3; 41 -5.9; 45 -5.7; 49 -5.4; 54 -5.2; 60 -5.1; 66 -5.0; 72 -5.0; 79 -5.1; 87 -5.2; 96 -5.4; 106 -5.5; 116 -5.7; 128 -5.8; 141 -5.8; 155 -5.8; 170 -5.7; 187 -5.5; 206 -5.5; 227 -5.6; 249 -5.4; 274 -5.3; 302 -5.2; 332 -5.1; 365 -5.0; 402 -5.1; 442 -5.2; 486 -5.2; 535 -5.0; 588 -4.8; 647 -4.8; 712 -4.6; 783 -4.1; 861 -3.4; 947 -2.9; 1042 -3.1; 1146 -3.8; 1261 -4.7; 1387 -5.4; 1526 -5.7; 1678 -5.6; 1846 -8.1; 2031 -9.1; 2234 -8.1; 2457 -6.9; 2703 -6.8; 2973 -7.4; 3270 -7.8; 3597 -7.6; 3957 -6.8; 4353 -6.3; 4788 -4.2; 5267 -0.5; 5793 -3.1; 6373 -3.5; 7010 -3.1; 7711 -4.8; 8482 -5.0; 9330 -5.0; 10263 -5.1; 11289 -5.1; 12418 -5.1; 13660 -7.3; 15026 -8.8; 16529 -8.8; 18182 -7.5; 20000 -5.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose SoundLink Around-Ear II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose SoundLink Around-Ear II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 974 Hz   | 2.86 | 2.5 dB  |
| Peaking | 2017 Hz  | 4.27 | -3.8 dB |
| Peaking | 3875 Hz  | 1.43 | -3.9 dB |
| Peaking | 5322 Hz  | 2.37 | 5.6 dB  |
| Peaking | 16308 Hz | 1.31 | -4.3 dB |
| Peaking | 26 Hz    | 1.39 | -2.0 dB |
| Peaking | 158 Hz   | 1.37 | -0.7 dB |
| Peaking | 11875 Hz | 4.1  | 1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.9 dB |
| Peaking | 62 Hz    | 1.41 | 0.6 dB  |
| Peaking | 125 Hz   | 1.41 | -0.8 dB |
| Peaking | 250 Hz   | 1.41 | -0.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.6 dB |
| Peaking | 4000 Hz  | 1.41 | -0.5 dB |
| Peaking | 8000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 16000 Hz | 1.41 | -4.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bose%20SoundLink%20Around-Ear%20II/Bose%20SoundLink%20Around-Ear%20II.png)