# Jabra Elite Active 65t

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.9; 25 5.5; 28 4.6; 31 3.7; 34 3.1; 37 2.6; 41 2.2; 45 1.9; 49 1.6; 54 1.3; 60 0.8; 66 0.3; 72 0.0; 79 -0.3; 87 -0.8; 96 -1.3; 106 -1.9; 116 -2.5; 128 -2.9; 141 -3.3; 155 -3.7; 170 -3.8; 187 -3.9; 206 -3.8; 227 -3.7; 249 -3.6; 274 -3.3; 302 -2.9; 332 -2.6; 365 -2.3; 402 -2.1; 442 -1.5; 486 -0.9; 535 -0.3; 588 0.4; 647 1.2; 712 1.6; 783 1.3; 861 0.7; 947 0.3; 1042 -0.3; 1146 -1.0; 1261 -1.3; 1387 -1.3; 1526 -1.3; 1678 -1.5; 1846 -1.9; 2031 -2.1; 2234 -1.7; 2457 -1.1; 2703 -0.5; 2973 -0.1; 3270 0.1; 3597 0.3; 3957 0.3; 4353 -0.5; 4788 -0.5; 5267 0.4; 5793 1.7; 6373 1.7; 7010 1.9; 7711 0.2; 8482 -3.7; 9330 -9.0; 10263 -10.4; 11289 -5.1; 12418 -0.1; 13660 0.0; 15026 0.0; 16529 -0.7; 18182 -0.9; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jabra Elite Active 65t GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jabra Elite Active 65t ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 18 Hz    | 0.7  | 6.4 dB   |
| Peaking | 187 Hz   | 0.85 | -4.4 dB  |
| Peaking | 1923 Hz  | 2.32 | -2.1 dB  |
| Peaking | 6837 Hz  | 2.55 | 3.4 dB   |
| Peaking | 9877 Hz  | 3.46 | -12.2 dB |
| Peaking | 386 Hz   | 2.17 | -0.9 dB  |
| Peaking | 711 Hz   | 2.18 | 2.3 dB   |
| Peaking | 1237 Hz  | 3.78 | -1.1 dB  |
| Peaking | 13146 Hz | 2.54 | 2.7 dB   |
| Peaking | 14213 Hz | 0.66 | -1.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Jabra%20Elite%20Active%2065t/Jabra%20Elite%20Active%2065t.png)