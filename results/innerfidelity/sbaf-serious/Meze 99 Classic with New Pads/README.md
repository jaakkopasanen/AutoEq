# Meze 99 Classic with New Pads

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.5dB
GraphicEQ: 21 0.0; 23 3.9; 25 3.0; 28 1.8; 31 0.7; 34 -0.2; 37 -0.9; 41 -1.5; 45 -2.0; 49 -2.4; 54 -2.8; 60 -3.1; 66 -3.5; 72 -3.7; 79 -3.8; 87 -3.6; 96 -3.5; 106 -3.1; 116 -2.9; 128 -3.7; 141 -4.2; 155 -4.6; 170 -3.5; 187 -4.0; 206 -4.1; 227 -3.9; 249 -3.5; 274 -2.9; 302 -2.5; 332 -2.3; 365 -2.1; 402 -2.4; 442 -2.5; 486 -2.7; 535 -2.8; 588 -2.4; 647 -2.3; 712 -2.0; 783 -1.3; 861 -1.0; 947 -0.4; 1042 0.3; 1146 -0.2; 1261 -0.3; 1387 -1.3; 1526 -2.8; 1678 -4.3; 1846 -4.4; 2031 -3.5; 2234 -2.9; 2457 -2.2; 2703 -1.4; 2973 -0.6; 3270 0.3; 3597 1.7; 3957 3.5; 4353 0.6; 4788 0.6; 5267 3.4; 5793 3.0; 6373 2.2; 7010 1.2; 7711 -0.1; 8482 -1.2; 9330 -2.8; 10263 -3.4; 11289 -2.2; 12418 -1.1; 13660 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Meze 99 Classic with New Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-54**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Meze 99 Classic with New Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 1.35 | 5.9 dB  |
| Peaking | 57 Hz    | 0.97 | -2.0 dB |
| Peaking | 179 Hz   | 0.38 | -3.6 dB |
| Peaking | 1846 Hz  | 3.16 | -4.7 dB |
| Peaking | 10189 Hz | 4.31 | -4.0 dB |
| Peaking | 604 Hz   | 2.75 | -1.1 dB |
| Peaking | 1056 Hz  | 4.39 | 1.3 dB  |
| Peaking | 5662 Hz  | 1.39 | 2.2 dB  |
| Peaking | 6093 Hz  | 1.84 | 1.6 dB  |
| Peaking | 8298 Hz  | 1.58 | -1.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Meze%2099%20Classic%20with%20New%20Pads/Meze%2099%20Classic%20with%20New%20Pads.png)