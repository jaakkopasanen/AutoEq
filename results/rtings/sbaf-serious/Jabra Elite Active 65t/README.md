# Jabra Elite Active 65t

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 5.7; 28 4.7; 31 3.8; 34 3.0; 37 2.5; 41 2.0; 45 1.6; 49 1.3; 54 1.0; 60 0.5; 66 0.2; 72 0.0; 79 -0.1; 87 -0.5; 96 -0.8; 106 -1.4; 116 -1.9; 128 -2.4; 141 -2.8; 155 -3.0; 170 -3.2; 187 -3.3; 206 -3.3; 227 -3.3; 249 -3.0; 274 -2.6; 302 -2.1; 332 -1.6; 365 -1.3; 402 -1.0; 442 -0.4; 486 0.3; 535 0.9; 588 1.5; 647 2.2; 712 2.5; 783 1.7; 861 0.8; 947 0.3; 1042 -0.2; 1146 -0.8; 1261 -1.0; 1387 -1.3; 1526 -1.7; 1678 -1.9; 1846 -1.8; 2031 -1.7; 2234 -1.2; 2457 -0.6; 2703 0.1; 2973 0.9; 3270 2.0; 3597 2.5; 3957 1.5; 4353 -0.5; 4788 -0.7; 5267 0.8; 5793 3.1; 6373 4.2; 7010 2.5; 7711 0.3; 8482 -3.3; 9330 -7.5; 10263 -7.0; 11289 -0.9; 12418 0.0
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

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 0.86 | 6.2 dB  |
| Peaking | 189 Hz   | 0.81 | -3.6 dB |
| Peaking | 665 Hz   | 2.94 | 3.1 dB  |
| Peaking | 6449 Hz  | 3.62 | 5.2 dB  |
| Peaking | 9620 Hz  | 4    | -9.3 dB |
| Peaking | 880 Hz   | 1.07 | 0.9 dB  |
| Peaking | 1762 Hz  | 0.88 | -2.5 dB |
| Peaking | 3601 Hz  | 1.99 | 3.7 dB  |
| Peaking | 4596 Hz  | 4.32 | -2.9 dB |
| Peaking | 11902 Hz | 7.12 | 1.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Jabra%20Elite%20Active%2065t/Jabra%20Elite%20Active%2065t.png)