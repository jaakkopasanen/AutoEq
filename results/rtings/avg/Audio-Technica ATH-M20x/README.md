# Audio-Technica ATH-M20x
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.7; 25 -1.1; 28 -2.2; 31 -3.2; 34 -4.1; 37 -4.8; 41 -5.6; 45 -6.3; 49 -6.9; 54 -7.7; 60 -8.4; 66 -8.9; 72 -9.1; 79 -9.1; 87 -9.0; 96 -9.0; 106 -9.2; 116 -9.3; 128 -9.3; 141 -8.8; 155 -8.0; 170 -6.9; 187 -5.7; 206 -4.2; 227 -3.0; 249 -2.7; 274 -3.8; 302 -5.1; 332 -5.8; 365 -6.4; 402 -6.9; 442 -7.3; 486 -7.5; 535 -7.6; 588 -7.5; 647 -7.4; 712 -7.1; 783 -6.8; 861 -6.6; 947 -6.5; 1042 -6.3; 1146 -6.5; 1261 -7.0; 1387 -7.6; 1526 -8.3; 1678 -8.9; 1846 -9.8; 2031 -10.4; 2234 -9.8; 2457 -8.4; 2703 -7.2; 2973 -6.8; 3270 -6.0; 3597 -3.2; 3957 -1.5; 4353 -3.0; 4788 -1.8; 5267 -0.5; 5793 -0.5; 6373 -1.3; 7010 -6.0; 7711 -9.0; 8482 -9.0; 9330 -6.7; 10263 -6.5; 11289 -6.7; 12418 -8.1; 13660 -7.4; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-M20x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-M20x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 0.83 | 7.1 dB  |
| Peaking | 115 Hz   | 0.32 | -4.1 dB |
| Peaking | 236 Hz   | 1.71 | 7.1 dB  |
| Peaking | 2027 Hz  | 2.54 | -4.3 dB |
| Peaking | 5044 Hz  | 2.06 | 6.4 dB  |
| Peaking | 3795 Hz  | 9.25 | 4.4 dB  |
| Peaking | 6288 Hz  | 3.41 | 7.1 dB  |
| Peaking | 7620 Hz  | 1.22 | -6.9 dB |
| Peaking | 9724 Hz  | 2    | 3.3 dB  |
| Peaking | 12621 Hz | 5.01 | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB  |
| Peaking | 62 Hz    | 1.41 | -2.9 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | 4.3 dB  |
| Peaking | 500 Hz   | 1.41 | -2.2 dB |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.2 dB |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-M20x/Audio-Technica%20ATH-M20x.png)