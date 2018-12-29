# Beats urBeats
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.2dB
GraphicEQ: 21 -5.7; 23 -5.8; 25 -5.8; 28 -5.9; 31 -6.0; 34 -6.1; 37 -6.2; 41 -6.3; 45 -6.5; 49 -6.6; 54 -6.9; 60 -7.3; 66 -7.6; 72 -7.9; 79 -8.2; 87 -8.6; 96 -9.0; 106 -9.6; 116 -10.1; 128 -10.5; 141 -10.8; 155 -11.0; 170 -10.9; 187 -10.8; 206 -10.6; 227 -10.6; 249 -10.5; 274 -9.9; 302 -9.2; 332 -8.5; 365 -7.8; 402 -7.1; 442 -6.3; 486 -5.4; 535 -4.4; 588 -3.3; 647 -2.2; 712 -1.2; 783 -0.3; 861 0.1; 947 0.2; 1042 -0.1; 1146 -0.5; 1261 -0.7; 1387 -0.5; 1526 -0.5; 1678 -0.6; 1846 -0.8; 2031 -0.8; 2234 -0.0; 2457 1.1; 2703 1.6; 2973 1.4; 3270 0.6; 3597 -0.5; 3957 -1.6; 4353 -3.1; 4788 -4.4; 5267 -5.8; 5793 -4.3; 6373 -0.8; 7010 2.1; 7711 0.3; 8482 0.0; 9330 -0.2; 10263 -4.0; 11289 -1.3; 12418 0.0; 13660 -0.1; 15026 -2.8; 16529 -0.4; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats urBeats GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-22**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats urBeats ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 36 Hz    | 0.21 | -5.6 dB |
| Peaking | 163 Hz   | 0.73 | -7.1 dB |
| Peaking | 330 Hz   | 1.21 | -4.7 dB |
| Peaking | 5186 Hz  | 4.07 | -6.3 dB |
| Peaking | 15133 Hz | 4.3  | -3.0 dB |
| Peaking | 509 Hz   | 3.87 | -1.0 dB |
| Peaking | 843 Hz   | 2.94 | 1.6 dB  |
| Peaking | 2848 Hz  | 3.89 | 2.5 dB  |
| Peaking | 7133 Hz  | 2.67 | 5.4 dB  |
| Peaking | 7643 Hz  | 1    | -3.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Beats%20urBeats/Beats%20urBeats.png)