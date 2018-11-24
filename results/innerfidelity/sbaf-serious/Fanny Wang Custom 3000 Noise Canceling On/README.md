# Fanny Wang Custom 3000 Noise Canceling On

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.7; 25 4.5; 28 2.9; 31 2.8; 34 3.6; 37 4.5; 41 5.1; 45 5.4; 49 5.5; 54 5.4; 60 5.0; 66 4.6; 72 4.2; 79 3.7; 87 3.1; 96 2.2; 106 1.3; 116 0.7; 128 -0.2; 141 -1.0; 155 -1.3; 170 -1.5; 187 -2.2; 206 -2.6; 227 -2.6; 249 -2.9; 274 -2.8; 302 -2.7; 332 -2.6; 365 -2.0; 402 -2.0; 442 -1.6; 486 -1.7; 535 -1.3; 588 -0.5; 647 0.3; 712 1.2; 783 1.7; 861 0.9; 947 0.5; 1042 -0.3; 1146 -1.3; 1261 -2.6; 1387 -3.7; 1526 -3.7; 1678 -2.5; 1846 -0.3; 2031 2.0; 2234 3.9; 2457 4.3; 2703 1.5; 2973 -3.8; 3270 -5.6; 3597 -3.2; 3957 -2.1; 4353 -3.1; 4788 -2.2; 5267 -0.8; 5793 1.6; 6373 2.6; 7010 2.0; 7711 -1.8; 8482 -7.2; 9330 -9.4; 10263 -7.6; 11289 -2.3; 12418 0.0; 13660 0.0; 15026 -2.0; 16529 -0.8; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fanny Wang Custom 3000 Noise Canceling On GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fanny Wang Custom 3000 Noise Canceling On ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 19 Hz   | 1.44 | 5.9 dB   |
| Peaking | 54 Hz   | 1.55 | 5.6 dB   |
| Peaking | 2341 Hz | 3.16 | 13.3 dB  |
| Peaking | 2460 Hz | 1.05 | -7.8 dB  |
| Peaking | 9470 Hz | 4.34 | -10.5 dB |
| Peaking | 271 Hz  | 0.99 | -3.1 dB  |
| Peaking | 801 Hz  | 2.58 | 2.7 dB   |
| Peaking | 1410 Hz | 5    | -2.5 dB  |
| Peaking | 6557 Hz | 3.73 | 4.9 dB   |
| Peaking | 8416 Hz | 7.62 | -3.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fanny%20Wang%20Custom%203000%20Noise%20Canceling%20On/Fanny%20Wang%20Custom%203000%20Noise%20Canceling%20On.png)