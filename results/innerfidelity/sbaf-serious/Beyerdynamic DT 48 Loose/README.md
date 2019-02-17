# Beyerdynamic DT 48 Loose
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -1.0; 79 -1.9; 87 -2.7; 96 -2.4; 106 -4.5; 116 -5.6; 128 -7.1; 141 -8.0; 155 -8.9; 170 -9.6; 187 -10.9; 206 -11.4; 227 -11.1; 249 -10.8; 274 -10.4; 302 -10.1; 332 -9.0; 365 -8.4; 402 -7.2; 442 -5.7; 486 -4.8; 535 -3.7; 588 -2.2; 647 -2.4; 712 -3.4; 783 -3.7; 861 -4.8; 947 -5.6; 1042 -7.3; 1146 -9.3; 1261 -10.7; 1387 -11.5; 1526 -12.6; 1678 -13.7; 1846 -13.9; 2031 -13.8; 2234 -12.6; 2457 -9.7; 2703 -6.9; 2973 -5.8; 3270 -5.5; 3597 -4.4; 3957 -3.0; 4353 -3.1; 4788 -1.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -9.7; 8482 -13.9; 9330 -11.5; 10263 -7.6; 11289 -6.5; 12418 -6.5; 13660 -6.6; 15026 -12.4; 16529 -15.8; 18182 -14.6; 20000 -9.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 48 Loose GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 48 Loose ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 39 Hz    | 0.85 | 7.3 dB   |
| Peaking | 1892 Hz  | 1.73 | -10.1 dB |
| Peaking | 7255 Hz  | 0.63 | 12.1 dB  |
| Peaking | 8466 Hz  | 2.31 | -18.4 dB |
| Peaking | 17186 Hz | 0.95 | -11.2 dB |
| Peaking | 40 Hz    | 1.06 | -8.4 dB  |
| Peaking | 54 Hz    | 0.31 | 8.0 dB   |
| Peaking | 205 Hz   | 0.64 | -8.8 dB  |
| Peaking | 622 Hz   | 1.21 | 6.2 dB   |
| Peaking | 1269 Hz  | 3.05 | -2.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB  |
| Peaking | 62 Hz    | 1.41 | 6.0 dB  |
| Peaking | 125 Hz   | 1.41 | -0.3 dB |
| Peaking | 250 Hz   | 1.41 | -6.7 dB |
| Peaking | 500 Hz   | 1.41 | 4.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -9.8 dB |
| Peaking | 4000 Hz  | 1.41 | 7.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB |
| Peaking | 16000 Hz | 1.41 | -8.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%2048%20Loose/Beyerdynamic%20DT%2048%20Loose.png)