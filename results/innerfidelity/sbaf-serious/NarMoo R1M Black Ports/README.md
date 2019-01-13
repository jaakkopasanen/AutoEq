# NarMoo R1M Black Ports
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.5dB
GraphicEQ: 21 -12.8; 23 -12.8; 25 -12.8; 28 -12.7; 31 -12.6; 34 -12.5; 37 -12.5; 41 -12.4; 45 -12.3; 49 -12.3; 54 -12.2; 60 -12.2; 66 -12.2; 72 -12.1; 79 -12.1; 87 -12.1; 96 -12.1; 106 -11.8; 116 -11.5; 128 -11.3; 141 -11.0; 155 -10.6; 170 -10.2; 187 -9.6; 206 -9.1; 227 -8.4; 249 -7.8; 274 -7.1; 302 -6.3; 332 -5.5; 365 -4.7; 402 -4.0; 442 -3.0; 486 -2.3; 535 -1.3; 588 -0.3; 647 0.2; 712 0.4; 783 0.6; 861 0.1; 947 0.2; 1042 -0.0; 1146 -0.2; 1261 -0.4; 1387 -0.7; 1526 -1.1; 1678 -1.3; 1846 -1.2; 2031 -0.9; 2234 -0.7; 2457 -0.3; 2703 -0.6; 2973 -0.9; 3270 -1.0; 3597 -1.4; 3957 -2.6; 4353 -5.5; 4788 -8.0; 5267 -7.5; 5793 -3.1; 6373 0.8; 7010 2.2; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -2.5; 18182 -1.7; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NarMoo R1M Black Ports GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-25**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NarMoo R1M Black Ports ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 0.2  | -12.5 dB |
| Peaking | 169 Hz   | 0.7  | -5.2 dB  |
| Peaking | 5054 Hz  | 2.72 | -10.5 dB |
| Peaking | 6444 Hz  | 2.26 | 4.5 dB   |
| Peaking | 17194 Hz | 3.52 | -3.2 dB  |
| Peaking | 48 Hz    | 2.29 | 0.2 dB   |
| Peaking | 349 Hz   | 1.82 | -1.1 dB  |
| Peaking | 690 Hz   | 1.55 | 1.9 dB   |
| Peaking | 1677 Hz  | 2.9  | -1.1 dB  |
| Peaking | 3567 Hz  | 6.09 | 0.6 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NarMoo%20R1M%20Black%20Ports/NarMoo%20R1M%20Black%20Ports.png)