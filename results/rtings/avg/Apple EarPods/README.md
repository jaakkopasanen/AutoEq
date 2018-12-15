# Apple EarPods

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 5.3; 49 4.1; 54 2.8; 60 1.3; 66 -0.0; 72 -1.1; 79 -2.1; 87 -3.0; 96 -3.6; 106 -3.9; 116 -4.1; 128 -4.1; 141 -3.9; 155 -3.9; 170 -3.7; 187 -3.4; 206 -3.1; 227 -2.9; 249 -2.7; 274 -2.6; 302 -2.4; 332 -2.4; 365 -2.4; 402 -2.4; 442 -2.2; 486 -2.1; 535 -1.9; 588 -1.8; 647 -1.3; 712 -0.6; 783 0.1; 861 0.4; 947 0.3; 1042 -0.2; 1146 -0.9; 1261 -1.9; 1387 -3.0; 1526 -4.1; 1678 -4.9; 1846 -5.4; 2031 -5.3; 2234 -4.6; 2457 -3.7; 2703 -2.9; 2973 -2.2; 3270 -1.4; 3597 -1.2; 3957 -1.5; 4353 -2.5; 4788 -3.6; 5267 -5.4; 5793 -7.9; 6373 -7.9; 7010 -5.6; 7711 -4.0; 8482 -2.7; 9330 -1.3; 10263 0.0; 11289 0.0; 12418 -0.6; 13660 -4.9; 15026 -3.9; 16529 -0.2; 18182 0.0; 20000 -1.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Apple EarPods GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Apple EarPods ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 42 Hz    | 0.44 | 13.7 dB  |
| Peaking | 83 Hz    | 0.43 | -11.8 dB |
| Peaking | 1916 Hz  | 1.9  | -5.6 dB  |
| Peaking | 6140 Hz  | 2.41 | -8.3 dB  |
| Peaking | 14227 Hz | 4.46 | -5.8 dB  |
| Peaking | 551 Hz   | 1.77 | -1.1 dB  |
| Peaking | 881 Hz   | 1.91 | 1.8 dB   |
| Peaking | 1447 Hz  | 4.45 | -1.1 dB  |
| Peaking | 8317 Hz  | 4.12 | -1.0 dB  |
| Peaking | 10586 Hz | 2.95 | 1.4 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Apple%20EarPods/Apple%20EarPods.png)