# Audeze Mobius

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.3dB
GraphicEQ: 21 -2.2; 23 -1.9; 25 -1.7; 28 -1.4; 31 -1.2; 34 -1.2; 37 -1.3; 41 -1.4; 45 -1.2; 49 -1.0; 54 -0.7; 60 -0.5; 66 -0.4; 72 -0.3; 79 -0.3; 87 -0.3; 96 -0.5; 106 -0.6; 116 -0.8; 128 -0.9; 141 -1.1; 155 -1.3; 170 -1.4; 187 -1.4; 206 -1.4; 227 -1.3; 249 -1.2; 274 -1.1; 302 -0.8; 332 -0.4; 365 -0.1; 402 0.3; 442 0.6; 486 0.1; 535 -0.5; 588 -0.8; 647 -0.7; 712 -0.5; 783 -0.7; 861 -0.6; 947 -0.2; 1042 0.0; 1146 -0.4; 1261 -0.7; 1387 -0.5; 1526 -0.8; 1678 -1.6; 1846 -2.2; 2031 -2.1; 2234 -1.4; 2457 -1.2; 2703 -1.6; 2973 -1.9; 3270 -2.1; 3597 -0.1; 3957 5.5; 4353 5.6; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.4; 7010 2.5; 7711 0.2; 8482 -3.3; 9330 -4.6; 10263 -3.1; 11289 -0.2; 12418 0.0; 13660 0.0; 15026 -2.1; 16529 -6.0; 18182 -6.0; 20000 -4.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze Mobius GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-62**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze Mobius ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 22 Hz    |  0.05 | -1.0 dB  |
| Peaking | 3279 Hz  |  0.63 | -18.5 dB |
| Peaking | 4399 Hz  |  0.55 | 21.6 dB  |
| Peaking | 9078 Hz  |  2.26 | -9.4 dB  |
| Peaking | 17698 Hz |  1.11 | -8.2 dB  |
| Peaking | 21 Hz    |  2.01 | -1.1 dB  |
| Peaking | 398 Hz   |  0.95 | -1.7 dB  |
| Peaking | 413 Hz   |  2.03 | 2.7 dB   |
| Peaking | 3470 Hz  |  8.41 | -1.8 dB  |
| Peaking | 3979 Hz  | 11.55 | 2.4 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Audeze%20Mobius/Audeze%20Mobius.png)