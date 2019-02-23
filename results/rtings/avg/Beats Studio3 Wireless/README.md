# Beats Studio3 Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.0; 23 -3.5; 25 -3.9; 28 -4.6; 31 -5.3; 34 -5.8; 37 -6.3; 41 -6.9; 45 -7.3; 49 -7.8; 54 -8.5; 60 -9.2; 66 -9.8; 72 -10.0; 79 -10.0; 87 -9.9; 96 -9.5; 106 -9.1; 116 -8.7; 128 -8.5; 141 -8.6; 155 -8.9; 170 -9.2; 187 -9.6; 206 -9.8; 227 -10.2; 249 -10.6; 274 -11.0; 302 -11.2; 332 -11.6; 365 -11.6; 402 -10.8; 442 -9.5; 486 -7.9; 535 -6.3; 588 -5.0; 647 -4.5; 712 -5.2; 783 -5.4; 861 -5.8; 947 -6.3; 1042 -5.8; 1146 -5.4; 1261 -5.4; 1387 -5.2; 1526 -4.9; 1678 -4.7; 1846 -4.6; 2031 -4.3; 2234 -3.4; 2457 -2.6; 2703 -3.4; 2973 -6.5; 3270 -8.3; 3597 -8.1; 3957 -5.4; 4353 -2.5; 4788 -0.5; 5267 -1.3; 5793 -2.0; 6373 -3.9; 7010 -4.8; 7711 -6.2; 8482 -6.5; 9330 -6.6; 10263 -8.4; 11289 -10.7; 12418 -10.8; 13660 -7.9; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Studio3 Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Studio3 Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 1.7  | 4.3 dB   |
| Peaking | 397 Hz   | 0.36 | -27.3 dB |
| Peaking | 494 Hz   | 0.34 | 24.2 dB  |
| Peaking | 5153 Hz  | 3.2  | 5.9 dB   |
| Peaking | 11822 Hz | 2.9  | -5.4 dB  |
| Peaking | 75 Hz    | 2.38 | -1.6 dB  |
| Peaking | 137 Hz   | 1.85 | 1.1 dB   |
| Peaking | 965 Hz   | 3.45 | -1.3 dB  |
| Peaking | 2874 Hz  | 1.46 | 4.6 dB   |
| Peaking | 3281 Hz  | 3.31 | -7.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.7 dB  |
| Peaking | 62 Hz    | 1.41 | -3.8 dB |
| Peaking | 125 Hz   | 1.41 | -0.8 dB |
| Peaking | 250 Hz   | 1.41 | -4.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -1.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Beats%20Studio3%20Wireless/Beats%20Studio3%20Wireless.png)