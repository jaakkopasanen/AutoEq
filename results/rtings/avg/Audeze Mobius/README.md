# Audeze Mobius

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.1dB
GraphicEQ: 21 -2.2; 23 -1.9; 25 -1.7; 28 -1.4; 31 -1.2; 34 -1.2; 37 -1.3; 41 -1.4; 45 -1.2; 49 -1.0; 54 -0.7; 60 -0.5; 66 -0.4; 72 -0.3; 79 -0.3; 87 -0.3; 96 -0.5; 106 -0.6; 116 -0.8; 128 -0.9; 141 -1.1; 155 -1.3; 170 -1.4; 187 -1.4; 206 -1.4; 227 -1.3; 249 -1.2; 274 -1.1; 302 -0.8; 332 -0.4; 365 -0.1; 402 0.3; 442 0.6; 486 0.1; 535 -0.5; 588 -0.8; 647 -0.7; 712 -0.5; 783 -0.7; 861 -0.6; 947 -0.2; 1042 0.0; 1146 -0.4; 1261 -0.7; 1387 -0.5; 1526 -0.8; 1678 -1.6; 1846 -2.2; 2031 -2.1; 2234 -1.4; 2457 -1.3; 2703 -1.8; 2973 -2.4; 3270 -2.9; 3597 -1.1; 3957 4.3; 4353 4.3; 4788 4.6; 5267 4.1; 5793 4.3; 6373 4.3; 7010 2.3; 7711 -0.0; 8482 -2.4; 9330 -1.9; 10263 -0.9; 11289 -0.6; 12418 0.0; 13660 -0.2; 15026 -4.7; 16529 -9.0; 18182 -10.4; 20000 -10.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze Mobius GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-50**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze Mobius ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 15 Hz    | 0.04 | -1.0 dB  |
| Peaking | 3590 Hz  | 1.13 | -5.9 dB  |
| Peaking | 4246 Hz  | 2.55 | 9.6 dB   |
| Peaking | 6012 Hz  | 3.09 | 5.3 dB   |
| Peaking | 18566 Hz | 1.11 | -11.8 dB |
| Peaking | 21 Hz    | 1.83 | -1.3 dB  |
| Peaking | 378 Hz   | 0.94 | -1.4 dB  |
| Peaking | 409 Hz   | 2.16 | 2.4 dB   |
| Peaking | 8712 Hz  | 6.38 | -2.6 dB  |
| Peaking | 13020 Hz | 3.95 | 2.9 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audeze%20Mobius/Audeze%20Mobius.png)