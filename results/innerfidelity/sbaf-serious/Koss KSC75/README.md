# Koss KSC75
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.6; 45 -1.2; 49 -2.2; 54 -3.3; 60 -4.5; 66 -5.6; 72 -6.5; 79 -7.4; 87 -8.3; 96 -9.0; 106 -9.5; 116 -9.7; 128 -9.9; 141 -9.9; 155 -10.0; 170 -9.7; 187 -9.5; 206 -9.4; 227 -9.2; 249 -9.0; 274 -8.6; 302 -8.3; 332 -8.0; 365 -7.7; 402 -7.4; 442 -7.0; 486 -6.9; 535 -6.8; 588 -6.3; 647 -6.3; 712 -6.3; 783 -6.0; 861 -6.2; 947 -6.4; 1042 -6.5; 1146 -6.6; 1261 -7.0; 1387 -7.9; 1526 -9.0; 1678 -9.8; 1846 -10.8; 2031 -11.4; 2234 -12.2; 2457 -12.0; 2703 -10.7; 2973 -9.4; 3270 -9.4; 3597 -1.4; 3957 -1.1; 4353 -10.8; 4788 -15.8; 5267 -9.3; 5793 -5.1; 6373 -4.8; 7010 -4.7; 7711 -6.6; 8482 -10.4; 9330 -13.1; 10263 -11.4; 11289 -6.7; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -8.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss KSC75 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss KSC75 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 30 Hz    | 1.53 | 7.4 dB   |
| Peaking | 2724 Hz  | 0.94 | -15.9 dB |
| Peaking | 3990 Hz  | 1.09 | 23.4 dB  |
| Peaking | 4641 Hz  | 3.64 | -21.2 dB |
| Peaking | 9435 Hz  | 3.04 | -9.8 dB  |
| Peaking | 50 Hz    | 1.8  | 3.4 dB   |
| Peaking | 132 Hz   | 0.61 | -3.8 dB  |
| Peaking | 812 Hz   | 1.06 | 1.7 dB   |
| Peaking | 6403 Hz  | 4.23 | 1.3 dB   |
| Peaking | 10857 Hz | 0.03 | -0.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.8 dB  |
| Peaking | 62 Hz    | 1.41 | 0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.7 dB |
| Peaking | 4000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20KSC75/Koss%20KSC75.png)