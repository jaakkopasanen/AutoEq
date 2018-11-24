# Beats urBeats

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.0dB
GraphicEQ: 21 -5.3; 23 -5.4; 25 -5.6; 28 -5.8; 31 -6.0; 34 -6.1; 37 -6.3; 41 -6.5; 45 -6.7; 49 -6.9; 54 -7.2; 60 -7.5; 66 -7.8; 72 -7.9; 79 -8.0; 87 -8.2; 96 -8.6; 106 -9.1; 116 -9.6; 128 -10.0; 141 -10.3; 155 -10.4; 170 -10.3; 187 -10.2; 206 -10.1; 227 -10.1; 249 -9.9; 274 -9.2; 302 -8.4; 332 -7.6; 365 -6.8; 402 -6.0; 442 -5.2; 486 -4.2; 535 -3.2; 588 -2.3; 647 -1.2; 712 -0.3; 783 0.2; 861 0.2; 947 0.2; 1042 -0.1; 1146 -0.3; 1261 -0.4; 1387 -0.5; 1526 -0.8; 1678 -0.9; 1846 -0.7; 2031 -0.4; 2234 0.4; 2457 1.5; 2703 2.5; 2973 2.9; 3270 3.2; 3597 2.7; 3957 0.9; 4353 -1.8; 4788 -2.8; 5267 -2.8; 5793 -0.4; 6373 2.9; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -0.2; 10263 -2.4; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats urBeats GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-39**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats urBeats ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 46 Hz    | 0.3  | -6.1 dB |
| Peaking | 157 Hz   | 0.83 | -5.8 dB |
| Peaking | 296 Hz   | 1.17 | -5.1 dB |
| Peaking | 3261 Hz  | 2.16 | 3.7 dB  |
| Peaking | 4734 Hz  | 4.58 | -4.3 dB |
| Peaking | 474 Hz   | 3.06 | -1.0 dB |
| Peaking | 793 Hz   | 2.11 | 1.6 dB  |
| Peaking | 1705 Hz  | 2.79 | -1.2 dB |
| Peaking | 6665 Hz  | 8.17 | 4.4 dB  |
| Peaking | 10082 Hz | 8.4  | -2.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Beats%20urBeats/Beats%20urBeats.png)